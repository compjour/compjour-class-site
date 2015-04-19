
~~~py
from datetime import datetime
right_now = datetime.now()
utc_now = datetime.today().utcnow()
~~~


## Converting from string to datetime

~~~py
from datetime import datetime
datetime(2010, 1, 1, 0, 0)
~~~

## Converting from UTC to datetime

~~~py
from datetime import datetime
datetime.fromtimestamp(1489334268.295324)
~~~

## Getting the UTC datetime right now

~~~py
from datetime import datetime
datetime.today().timestamp()
~~~



## Time differences

~~~py

~~~
