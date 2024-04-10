unit TASK2_SIN;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls;

type
  TForm3 = class(TForm)
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Button1: TButton;
    procedure solveIntegral(Sender: TObject);
  private
    { Private declarations }
    function f(x: Double): Double;
    function integral(a, b, h: Double): Double;
  public
    { Public declarations }

  end;

var
  Form3: TForm3;

implementation

{$R *.dfm}
function TForm3.f(x: Double): Double;
begin
  Result := Sin(x * x * x);
end;

function TForm3.integral(a, b, h: Double): Double;
var
  N, i: Integer;
  S1, S2, x: Double;
begin
  N := Round((b - a) / h);
  S1 := 0;
  for i := 0 to N - 1 do
  begin
    x := a + i * h;
    S1 := S1 + f(x);
  end;
  Result := S1 * h;
end;

procedure TForm3.solveIntegral(Sender: TObject);
var
  a, b, eps, h, S1, S2: Double;
  N, iterations: Integer;
begin
  a := StrToFloat(Edit1.Text);
  b := StrToFloat(Edit2.Text);
  eps := StrToFloat(Edit3.Text);

  N := 100;

  repeat
    h := (b - a) / N;
    S1 := integral(a, b, h);
    N := N * 2;
    h := (b - a) / N;
    S2 := integral(a, b, h);
    iterations := iterations + 1;
  until Abs(S1 - S2) <= eps;

  ShowMessage('Значение интеграла sin(x^3): ' + FloatToStr(S2) + ' Число итераций: ' + IntToStr(iterations));

end;
end.
