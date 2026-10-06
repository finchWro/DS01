local ooxml = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

function RawBlock (el)
  if el.text:match("^\\newpage") or el.text:match("^\\pagebreak") then
    return pandoc.RawBlock('openxml', ooxml)
  end
end

function Block (el)
  if el.classes and el.classes:includes('pagebreak') then
    return pandoc.RawBlock('openxml', ooxml)
  end
end
