// See https://aka.ms/new-console-template for more information
using System.Diagnostics;
using System.Reflection;

// After the MSIX package is insalled, the default running dir is C:\system32. This part guarantee that the running folder is the same folder as the instalation folder.
string exeDir = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
Directory.SetCurrentDirectory(exeDir);

// Execute python program
Process myProcess = new Process();
myProcess.StartInfo.UseShellExecute = false;
myProcess.StartInfo.FileName = @"user_gui.exe";
myProcess.Start();
