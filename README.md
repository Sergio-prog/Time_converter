# Time converter

Version 0.75b

Light and Fast Time converter class for Python

The program can convert such time values: *nanosecond, microsecond, millisecond, minute, hour, day, week, month, year,
century, second*

Also, you can pass parameters in the *datetime.timedelta* and *datetime.datetime* class form
---

# Code Example

```python
from converter import Time

weeks = Time(type_="week", value=5)
print(weeks.to_day())
# > 35.0
```