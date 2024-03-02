def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    today = datetime.today().date()
    
    # Створюємо словник для зберігання імен користувачів по днях тижня
    birthdays_per_week = defaultdict(list)
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        
        # Конвертуємо дату народження на поточний рік
        birthday_this_year = birthday.replace(year=today.year)
        
        # Оцінюємо дату народження на цей рік
        if birthday_this_year < today:
            # Якщо день народження вже минув, розглядаємо наступний рік
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Визначаємо різницю між днем народження та поточним днем
        delta_days = (birthday_this_year - today).days
        
        # Визначаємо день тижня дня народження
        birthday_weekday = (today.weekday() + delta_days) % 7
        
        # Якщо день народження випадає на вихідний, переносимо його на понеділок
        if birthday_weekday >= 5:
            birthday_weekday = 0  # Понеділок
        
        # Зберігаємо ім'я користувача в відповідний день тижня
        day_of_week = calendar.day_name[birthday_weekday]
        birthdays_per_week[day_of_week].append(name)
    
    # Виводимо зібрані імена по днях тижня у відповідному форматі
    for day, names in birthdays_per_week.items():
        names_str = ", ".join(names)
        print(f"{day}: {names_str}")
