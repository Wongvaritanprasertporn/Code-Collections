Sub ChangeVHDLColorInSelection()
    Dim rng As Range
    Dim vhdlWords As Variant
    Dim word As Variant
    Dim quoteRng As Range
    Dim singleQuoteRng As Range
    Dim commentRng As Range

    vhdlKeywords = Array("abs", "access", "after", "alias", "all", "and", "architecture", "array", "assert", "attribute", "begin", "end", "block", "body", "buffer",
                    "bus", "case", "component", "configuration", "constant", "disconnect", "downto", "else", "elsif", "end", "entity", "exit", "file", "for",
                    "function", "generate", "generic", "group", "guarded", "if", "impure", "in", "inertial", "inout", "is", "label", "library", "linkage", "buffer",
                    "inout", "literal", "loop", "map", "mod", "nand", "new", "next", "nor", "not", "null", "of", "on", "open", "or", "others", "out", "package",
                    "port", "postponed", "procedure", "process", "pure", "range", "to", "record", "register", "reject", "rem", "report", "return", "rol", "ror",
                    "select", "severity", "signal", "shared", "sla", "sll", "sra", "srl", "subtype", "then", "to", "transport", "type", "unaffected", "units", "until", "use",
                    "variable", "wait", "when", "while", "with", "xnor", "xor")
    vhdlLib = Array("ieee", "std_logic_1164", "std_logic_unsigned", "std_logic_textio", "std_logic_arith", "numeric_bit", "numeric_std", "std_logic_signed", "math_real", "math_complex")
    vhdlDataTypes = Array("integer", "real", "boolean", "bit", "bit_vector", "physical", "natural", "positive",  "std_logic","std_ulogic","bit_vector", "string", "std_logic_vector","std_ulogic_vector", "type", "array", "record" )

    Set rng = Selection.Range

    For Each word In vhdlkeywords
        With rng.Find
            .Text = " " & word & " "
            .Replacement.Text = word
            .Replacement.Font.Color = wdColorLightBlue
            .Forward = True
            .Wrap = wdFindContinue
            .Format = True
            .MatchCase = True
            .MatchWildcards = True ' Enable wildcard search
            .Execute Replace:=wdReplaceAll
        End With
    Next word

    For Each word In vhdl2
        With rng.Find
            .Text = " " & word & " "
            .Replacement.Text = word
            .Replacement.Font.Color = wdColorRed
            .Forward = True
            .Wrap = wdFindContinue
            .Format = True
            .MatchCase = True
            .MatchWildcards = True ' Enable wildcard search
            .Execute Replace:=wdReplaceAll
        End With
    Next word

    ' Find and change color of text inside double quotation marks
    Set quoteRng = rng.Duplicate ' Create a duplicate range for finding quoted text
    With quoteRng.Find
        .Text = """*"""
        .Replacement.Text = "^&" ' Replace with the found text (no changes)
        .Replacement.Font.Color = wdColorPink ' Change this color to purple for text in double quotes
        .Forward = True
        .Wrap = wdFindContinue
        .Format = True
        .MatchWildcards = True ' Enable wildcard search for text in quotes
        .Execute Replace:=wdReplaceAll
    End With

    ' Find and change color of text inside single quotation marks
    Set singleQuoteRng = rng.Duplicate ' Create a duplicate range for finding text in single quotes
    With singleQuoteRng.Find
        .Text = "'*'"
        .Replacement.Text = "^&" ' Replace with the found text (no changes)
        .Replacement.Font.Color = wdColorPink ' Change this color to purple for text in single quotes
        .Forward = True
        .Wrap = wdFindContinue
        .Format = True
        .MatchWildcards = True ' Enable wildcard search for text in single quotes
        .Execute Replace:=wdReplaceAll
    End With

    ' Find and change color of comments (from "--" to the end of the line)
    Set commentRng = rng.Duplicate ' Create a duplicate range for finding comments
    With commentRng.Find
        .Text = "--*^13"
        .Replacement.Text = "^&" ' Replace with the found text (no changes)
        .Replacement.Font.Color = wdColorGreen ' Change this color to green for comments
        .Forward = True
        .Wrap = wdFindContinue
        .Format = True
        .MatchWildcards = True ' Enable wildcard search for comments
        .Execute Replace:=wdReplaceAll
    End With
     ' Find and change color of package names (after "use")
    Set packageRng = rng.Duplicate ' Create a duplicate range for finding package names
    With packageRng.Find
        .Text = "use *;" ' Find the package names after "use"
        .Replacement.Text = "^&"
        .Replacement.Font.Color = wdColorRed ' Change this color to red for package names
        .Forward = True
        .Wrap = wdFindContinue
        .Format = True
        .MatchWildcards = True
        .Execute Replace:=wdReplaceAll
    End With

    ' Find and change color of declared names (after "signal", "variable", "constant")
    Set declaredNameRng = rng.Duplicate ' Create a duplicate range for finding declared names
    With declaredNameRng.Find
        .Text = "(signal|variable|constant) *:" ' Find declared names after signal, variable, or constant
        .Replacement.Text = "^&"
        .Replacement.Font.Color = wdColorRed ' Change this color to red for declared names
        .Forward = True
        .Wrap = wdFindContinue
        .Format = True
        .MatchWildcards = True
        .Execute Replace:=wdReplaceAll
    End With

    ' Find and change color of numbers not part of declared names
    Set numberRng = rng.Duplicate ' Create a duplicate range for finding numbers
    With numberRng.Find
        .Text = "<[0-9]@>" ' Find sequences of digits
        .Replacement.Text = "^&"
        .Replacement.Font.Color = wdColorRed ' Change this color to red for numbers
        .Forward = True
        .Wrap = wdFindContinue
        .Format = True
        .MatchWildcards = True
        .Execute Replace:=wdReplaceAll
    End With
End Sub
