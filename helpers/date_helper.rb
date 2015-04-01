def friendly_date(val)
  if (v = _to_date(val))
    v.strftime('%A, %B %-d')
  else
    val
  end
end


def date_slug(val)
  _to_date(val).strftime '%Y-%m-%d'
end

def machine_date(val)
  _to_date(val).andand.strftime '%Y-%m-%dT%l:%M:%S%z'
end

def simple_date(val)
  v.strftime('%B %-d')
end

def _to_date(val)
  d = case val
  when Date, Time
    val
  else
    Chronic.parse(val)
  end

  return d
end
