unit task1_delphi;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls;

type
    TForm3 = class(TForm)
    Label1: TLabel;
    Label2: TLabel;
    Edit1: TEdit;
    Button1: TButton;
    procedure solve(Sender: TObject);
  private
    { Private declarations }
    function FindRoot(a, b, c, eps : Double) : Double;
  public
    { Public declarations }

  end;

var
  Form3: TForm3;

implementation

{$R *.dfm}
function TForm3.FindRoot(a, b, c, eps : Double) : Double;
begin
  repeat
    Result := (a+b)/2;
    if(b-c)*(Result-c)<0 then
      a:=Result
    else
      b:=Result;
  until abs(b-a)<eps;
end;

procedure TForm3.solve(Sender: TObject);
var
  a, b, eps, c: Double;
begin
  a := -20;
  b := 30;
  c := 13.5;
  eps := StrToFloat(Edit1.Text);
  ShowMessage('Root is '  + FloatToStr(FindRoot(a,b,c,eps)));
end;
end.
