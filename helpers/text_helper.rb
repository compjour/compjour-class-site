
def make_markdown(str)
  Kramdown::Document.new(str.to_s).to_html
end

