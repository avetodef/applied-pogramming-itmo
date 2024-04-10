object Form3: TForm3
  Left = 0
  Top = 0
  Caption = 'Form3'
  ClientHeight = 155
  ClientWidth = 358
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  TextHeight = 15
  object Edit1: TEdit
    Left = 16
    Top = 32
    Width = 81
    Height = 23
    TabOrder = 0
    Text = 'a'
  end
  object Edit2: TEdit
    Left = 120
    Top = 32
    Width = 81
    Height = 23
    TabOrder = 1
    Text = 'b'
  end
  object Edit3: TEdit
    Left = 233
    Top = 32
    Width = 81
    Height = 23
    TabOrder = 2
    Text = 'epsilon'
  end
  object Button1: TButton
    Left = 16
    Top = 80
    Width = 298
    Height = 25
    Caption = 'solve integral of sin(x^3)'
    TabOrder = 3
    OnClick = solveIntegral
  end
end
