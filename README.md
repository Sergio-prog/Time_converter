# Time converter

Version 0.7b

Light and Fast Time converter class for Python

The program can convert such time values: *nanosecond, microsecond, millisecond, minute, hour, day, week, month, year,
century, second*

Also, you can pass parameters in the *time.timedelta* class form

---

# Code Example

```
weeks = Time(type_="week", value=5)

print(weeks.to_day())
```

```
35.0
```