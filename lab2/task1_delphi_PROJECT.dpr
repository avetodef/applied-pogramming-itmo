program task1_delphi_PROJECT;

uses
  Vcl.Forms,
  task1_delphi in 'task1_delphi.pas' {Form3};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TForm3, Form3);
  Application.Run;
end.
