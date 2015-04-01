def weeks
  wks = sitemap.resources.select{|s| s.url =~ /\/weeks\// }.sort_by{|s| s.data.week }
#  wks = wks.map{|w| w.data.start_date = first_day + (24 * 60 * 60 * 7 * w.data.week)}

  wks
end


def active_weeks
  weeks.select{|w| w.data.show_link == true}
end

def first_day
  Chronic.parse(config[:class_start_date])
end


def week_start_date_foo(w)
  first_day + (24 * 60 * 60 * 7 * (w.data.week - 1))
end


def this_week
  active_weeks[-1]
end
