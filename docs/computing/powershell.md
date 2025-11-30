# PowerShell
PowerShell (PS or pwsh) is a command-line shell and scripting language.

Instead of being a strictly compile/interpreted language, PowerShell compiles to an _abstract syntax tree_ (AST), which checks your code first before running it. It does not create an executable like compiled languages, nor does it interpret line-by-line like an interpreted language.

It is case-insensitive and is insensitive to data types when piping. All i/o is text-based, so fewer formatting operations are necessary.

## Cmdlets
Commands in PS are called cmdlets (commandlets). These are compiled commands that are built via `.NET`.
Cmdlets are named according to `verb-noun` syntax.
- `Get-Verb`: Shows all available verbs.
- `Get-Command`: Shows all available commands. We can refine this search further via: 
    - `Get-Command -Noun alias*`: Lists all commands with the noun `alias`.
    - `Get-Command -Verb Get -Noun alias*`: Lists all commands with the verb `Get` and the noun `alias`.
- `Get-Help`: Displays helpful information. 
    - For specific cmdlets, we can use `Get-Help <cmdlet>`.
    - Use `Update-Help` to update the documentation.
    - Altenatively, use `Get-Help <cmdlet> -Online` to view up-to-date help online. 

## Objects
Commandlets always return _objects_ which condense a lot more information than what is immediately presented.
Joining object outputs together with `|` forms a _pipeline_.
NB: Not all commands accept pipeline input. Use the `Get-Help` command and search for `Accept pipeline input?` to check this.

### Getting Object Information
To view additional information about an object, pipe the output into the `Get-Member` command.
```powershell
Get-Process -Name explorer | Get-Member
```

#### Viewing the Full Object Output
Use `Format-List` or `Format-Table`. 
```powershell
# Shows all _explorer_ object outputs.
Get-Process explorer | Format-List -Property *
```

```powershell
# Shows all _explorer_ object outputs beginning with "S".
Get-Process explorer | Get-Member -Name S*
```

`Format-List` also pretty-prints your output. E.g.
```powershell
Get-Process -Name explorer | Get-Member P* | Format-List
```
is more nicely formatted than
```powershell
Get-Process -Name explorer | Get-Member P*
```

#### Filtering Output
The `Select-Object` cmdlet can be used to filter columns from the `Get-Member` output. 
```powershell
Get-Process -Name explorer | Get-Member | Select-Object Name, MemberType
```
It can also be used to view hidden data columns that would otherwise not be presented.
```powershell
Get-Process explorer | Select-Object -Property Id, Name, CPU
```

#### Sorting Output
Use `Sort-Object` to sort the output.

```powershell
# Sorting by one column.
Get-Process | Sort-Object -Descending -Property Name
```

```powershell
#Sorting by two columns.
Get-Process | Sort-Object -Descending -Property Name, CPU
```

```powershell
# Sort via an expression.
Get-Process explorer | Get-Member | Sort-Object -Property @{Expression = "MemberType"; Descending = $True}
```

### Viewing Running Processes
The `Get-Process` command lists all of the processes that are running on the machine. `Get-Process -Name 'explorer'` filters that list to processes named "explorer". Thus, `Get-Member` elaborates on the `Get-Process` output.

## Best Practice: Filtering left, Formatting Right.
For efficiency, it is best to filter as early as possible in a pipeline, to minimise the data being handled.

In addition, it is better to format data at the end of a pipeline to ensure that no data is lost/misinterpreted during the formatting process. E.g.:

```powershell
Get-Process | Select-Object Name | Where-Object Name -eq explorer
```
is less efficient than
```powershell
Get-Process -Name explorer | Select-Object Name
```
because filtering to the "Name" column is occurring earlier in the pipeline.

Another example: Never pipe `Select-Object` after `Format-List` as it returns an empty list. This is because the outputs of a formatted list are _properties_, not objects.

## Creating files
Use `New-Item` to create files.
```powershell
New-Item TestScript.ps1
```

## Writing to the console
Use `Write-Output` to write to the console.
```powershell
Write-Output 'Hello World!'

# Output: Hello World!
```

## Running Scripts
Scripts may be run using `.\<ScriptName>.ps1`.

### Execution Policies
As a safety feature, Windows sets a _restricted execution policy_ that prevents scripts from running. To temporarily disable this for the current session, use:
```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```
Restrictions will be re-enabled once the session (the _Process_) is closed.

## Variable assignment
Use `$<variable_name>`.
```powershell
$name = 'Limi'
Write-Output $name

# Output: Limi
```

## User Input
Use `Read-Host`.
```powershell
$name = Read-Host -Prompt "Enter Name"
Write-Output "Hello $name!"

# Output: Enter Name: Limi
# Output: Hello Limi!
```

## Strings
Strings can be defined via `'` or `"`. However, `"` are needed to _interpolate_ (interpret and display) variables within a string. In other words `'` defines a _string literal_.

```powershell
$name = 'Limi'
Write-Output '$name'
Write-Output "$name"

# Output: $name
# Output: Limi
```

## Escape characters
Use the ` character to escape interpolation.
```powershell
$name = 'Limi'
Write-Output "`$name"

# Output: $name
```

## Expressions
These allow operations to be performed inside a string.
```powershell
Write-Output "$(3+1)"

# Output: 4
```

## Parameters
Parameters can be declared within a script to add further inputs.
```powershell
Param($Name)
Write-Host "Hello $name"
```
Which can then be called and supplied values via:
```powershell
.\TestScript.ps1 -Name Limi

# Output: Hello Limi
```

### Default Parameters
These can be provided as variable assignments.
```powershell
Param($Name = 'Limi')
Write-Host "Hello $name"
```

### Verifying parameter validity.
To ensure that the parameter is used correctly (e.g. correct data types supplied), you should use conditional statements to catch error cases.
```powershell
Param($Name)
if (-Not $Name -eq ''){Write-Host "Hello $name"}
Else {Write-Error "Empty input"}

# Input: Limi -> Output: Hello Limi
# Input: <Nothing> -> Output: <Error Message>
```
A more concise, equivalent statement utilises _decorators_. If the parameter isn't provided when the script is called, the user is prompted.
```powershell
Param( [Parameter(Mandatory)] $Name )
Write-Host "Hello $name"
```
An optional help message can also be added, which the user can access via `!?`
```powershell
Param([Parameter(Mandatory, HelpMessage = "Enter a name.")] $Name)
Write-Host "Hello $name"
```

#### Type control
The data type can be controlled similarly to a decorator.
```powershell
Param([Parameter(Mandatory, HelpMessage = "Enter a name.")] [string] $Name)
Write-Host "Hello $name"
```

## Bag-o-Tricks: Backup Script (Needs Testing)
```powershell
Param(
  [string]$Path = './app',
  [string]$DestinationPath = './'
)
If (-Not (Test-Path $Path)) 
{
  Throw "The source directory $Path does not exist, please specify an existing directory"
}
$date = Get-Date -format "yyyy-MM-dd"
$DestinationFile = "$($DestinationPath + 'backup-' + $date + '.zip')"
If (-Not (Test-Path $DestinationFile)) 
{
  Compress-Archive -Path $Path -CompressionLevel 'Fastest' -DestinationPath "$($DestinationPath + 'backup-' + $date)"
  Write-Host "Created backup at $($DestinationPath + 'backup-' + $date + '.zip')"
} Else {
  Write-Error "Today's backup already exists"
}
```

## Flow Control

### If Statements
```powershell
$i = 1
$j = 9
if ($i -le 5) {Write-Output 'i Correct'}
if ($j -le 5) {Write-Output 'j Correct'}

# Output: i Correct
```
### Else Statements
```powershell
$i = 1
$j = 9

if ($i -le 5) {Write-Output 'i Correct'}
Else {Write-Output 'i Incorrect'}

if ($j -le 5) {Write-Output 'j Correct'}
Else {Write-Output 'j Incorrect'}

# i Correct
# j Incorrect
```
### ElseIf Statements
```powershell
$i = 1
$j = 9

if ($i -le 5) {Write-Output 'i Correct'}
Else {Write-Output 'i Incorrect'}

if ($j -le 5) {Write-Output 'j Correct'}
ElseIf ($j -le 10) {Write-Output 'j Partially Correct'}
Else {Write-Output 'j Incorrect'}

# Output: i Correct
# Output: j Partially Correct
```

## Error Handling

### Try-Catch Statements
#### Catch all errors
```powershell
# Catches all console output errors and presents "INVALID" instead.
$i = 'a'
Try{Write-Output "$(1+$i)"}
Catch{Write-Output "INVALID"}
```
#### Catch Specific Errors
```powershell
# Catches a specific type of error. 
$i = 'a'
Try{Write-Output "$(1+$i)"} 
Catch [System.Management.Automation.RuntimeException] {Write-Output "INVALID"}
```
To catch multiple errors, use multiple catch statements.  

#### Finding Error Codes
```powershell
$i = 'a'
Try{Write-Output "$(1+$i)"} 
Catch {Write-Host "Exception Type:" $_.Exception.GetType().FullName}

# Output: Exception Type: System.Management.Automation.RuntimeException
```

### Try-Catch-Finally Statements
Finally, statements run regardless of whether or not an error has occurred.
```powershell
$i = 'a'
Try {Write-Output "$(1+$i)"} 
Catch [System.Management.Automation.RuntimeException] {Write-Output "INVALID"}
Finally {Write-Output "Done"}

# Output: INVALID
# Output: Done
```

### Custom Errors
Use `Write-Error` to raise a custom error message.
Use `-ErrorAction Stop` to escalate the error and stop the code.
```powershell
Try {Get-Content './dummy.txt' -ErrorAction Stop} 
Catch {Write-Error "File doesn't exist"}
```

`Throw` may also be used within conditional statements.
```powershell
$i = 1
If ($i -eq 1) {Throw "The forbidden Number"}
```

## Loops
INVESTIGATE OTHER LOOP STRUCTURES

```powershell
$items = 'a','b','c'
foreach ($item in $items) {Write-Output $item}

# Output: a
# Output: b
# Output: c
```

### Providing input as parameters
```powershell
Param([Parameter(Mandatory)][string[]]$items)
foreach ($item in $items) {Write-Output $item}

# Input: .\TestScript.ps1 -items 'a','b','c'
# Output: a
# Output: b
# Output: c
```
