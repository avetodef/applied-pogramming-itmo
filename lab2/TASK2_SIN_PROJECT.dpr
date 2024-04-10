program TASK2_SIN_PROJECT;

uses
  Vcl.Forms,
  TASK2_SIN in 'TASK2_SIN.pas' {Form3};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TForm3, Form3);
  Application.Run;
end.
