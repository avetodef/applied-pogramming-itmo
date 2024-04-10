program TASK1_PART2_PROJECT;

uses
  Vcl.Forms,
  TASK1_PART2_CORRECT in 'TASK1_PART2_CORRECT.pas' {Form3};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TForm3, Form3);
  Application.Run;
end.
