object Form3: TForm3
  Left = 0
  Top = 0
  Caption = 'Form3'
  ClientHeight = 175
  ClientWidth = 359
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  TextHeight = 15
  object Label1: TLabel
    Left = 40
    Top = 56
    Width = 37
    Height = 15
    Caption = 'a = -20'
  end
  object Label2: TLabel
    Left = 104
    Top = 56
    Width = 33
    Height = 15
    Caption = 'b = 30'
  end
  object Edit1: TEdit
    Left = 160
    Top = 56
    Width = 121
    Height = 23
    TabOrder = 0
    Text = 'epsilon'
  end
  object Button1: TButton
    Left = 40
    Top = 96
    Width = 241
    Height = 25
    Caption = 'solve'
    TabOrder = 1
    OnClick = solve
  end
end
