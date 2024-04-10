object Form3: TForm3
  Left = 0
  Top = 0
  Caption = 'Form3'
  ClientHeight = 264
  ClientWidth = 362
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  TextHeight = 15
  object Edit1: TEdit
    Left = 8
    Top = 32
    Width = 121
    Height = 23
    TabOrder = 0
    Text = 'A'
  end
  object Edit2: TEdit
    Left = 160
    Top = 32
    Width = 121
    Height = 23
    TabOrder = 1
    Text = 'B'
  end
  object Edit3: TEdit
    Left = 8
    Top = 72
    Width = 121
    Height = 23
    TabOrder = 2
    Text = 'Y'
  end
  object Edit4: TEdit
    Left = 160
    Top = 72
    Width = 121
    Height = 23
    TabOrder = 3
    Text = 'EPSILON'
  end
  object Button1: TButton
    Left = 8
    Top = 128
    Width = 273
    Height = 25
    Caption = 'SOLVE'
    TabOrder = 4
    OnClick = solve
  end
end
