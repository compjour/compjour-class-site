def homework_sections
  data.homework.sections
end

def assigned_homework
  arr = []
  data.homework.sections.each do |s|
    arr.concat(s.deliverables.select{|d| d.content_slug.present? })
  end

  arr
end


def todos
  data.todos
end
