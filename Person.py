from all_cities_links import taj_cities, rus_cities, ind_cities, uzb_cities, kaz_cities


class Person:
    def __init__(self):
        self.message = ' '
        self.start_keyboard = None
        self.name = ''
        self.username = ''
        self.user_id = 0
        self.country = ''
        self.city = ''
        self.url = ''
        self.sending_list = []

        self.taj_cities = taj_cities
        self.rus_cities = rus_cities
        self.ind_cities = ind_cities
        self.uzb_cities = uzb_cities
        self.kaz_cities = kaz_cities

    def parse_tj(self):
        import requests
        from bs4 import BeautifulSoup as BS
        url = self.taj_cities[self.city]
        self.url = url
        response = requests.get(url)

        # Create a soup object and find the tbody element
        soup = BS(response.text, 'html.parser')
        table_body = soup.find('tbody')

        # Find all the rows in the table body and create a list of lists
        rows = table_body.find_all('tr')
        namaz_data = []
        for row in rows:
            # Find all the cells in the row and create a list of cell values
            cells = row.find_all('td')
            row_data = []
            for cell in cells:
                # Append the text content of the cell to the row data list
                row_data.append(cell.text.strip())
            # Append the row data list to the table data list
            namaz_data.append(row_data)

        # Print the table data list
        b_time = f'<b>{namaz_data[0][1]} - {namaz_data[1][1]}</b>\n'
        p_time = f'<b>{namaz_data[2][1]}</b>\n'
        a_time = f'<b>{namaz_data[4][1]}</b>\n'
        sh_time = f'<b> {namaz_data[5][1]}</b>\n'
        kh_time = f'<b>{namaz_data[6][1]}</b>\n\n'
        bomdod = '🌅' + '{:<20}:     {:>12}'.format('<i> Бомдод</i>', b_time)
        peshin = '☀' + '{:<20}:     {:>12}'.format(f'<i> Пешин</i> ', p_time)
        asr = '⛅' + '{:<20}     :     {:>12}'.format(f'<i> Аср</i> ', a_time)
        shom = '🏙' + '{:<20}  :     {:>12}'.format(f'<i> Шом</i> ', sh_time)
        khuftan = '🌃' + '{:<19}:     {:>12}'.format(f'<i> Хуфтан</i> ', kh_time)
        sarchashma = f'<a href="{url}">Дидани сарчашма 👀</a>'
        self.message = f'Шаҳри шумо <b>{self.city}</b>\n\n' + bomdod + peshin + asr + shom + khuftan + sarchashma

    def parse_ru(self):
        import requests
        from bs4 import BeautifulSoup

        url = self.rus_cities[self.city]
        self.url = url
        response = requests.get(url)

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all divs with class="content"
        content_divs = soup.find_all('div', class_='content')

        # Extract the text from each content_div and append it to an array
        namaz_data = []
        for content_div in content_divs:
            namaz_data.append(content_div.text.strip())

        # Print the results
        t = namaz_data[15].split('\n')[3]
        bomdod = f'🌅<i> Фаджр</i>     :     <b>{namaz_data[5]} - {namaz_data[7]}</b>\n'
        peshin = f'☀<i> Зухр</i>          :     <b>{namaz_data[9]}</b>\n'
        asr = f"⛅<i> Аср</i>            :     <b>{namaz_data[11].split()[2].replace(')', '')}</b>\n"
        shom = f'🏙<i> Магриб</i>    :     <b> {namaz_data[13]}</b>\n'
        khuftan = f"🌃<i> Иша</i>          :      <b>{t}</b>\n\n"
        sarchashma = f'<a href="{url}">Посмотреть источник 👀</a>'
        self.message = f'Ваш город <b>{self.city}</b>\n\n' + bomdod + peshin + asr + shom + khuftan + sarchashma

    def parse_ind(self):
        from bs4 import BeautifulSoup
        import requests

        # Fetch the webpage HTML content
        url = self.ind_cities[self.city]
        self.url = url
        response = requests.get(url)
        html_content = response.text

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all div tags with class "prayerTiles"
        prayer_tiles = soup.find_all('div', class_='prayerTiles')

        # Extract information from each prayer tile and store in separate arrays
        namaz_data = []

        for prayer_tile in prayer_tiles:
            # Extract the prayer name and time
            prayer_name = prayer_tile.find('p').text.strip()

            # Add to the prayer names and times arrays
            namaz_data.append(prayer_name)

        # Print the prayer names and times
        b_time = namaz_data[0].split('\n')[1] + ' - ' + namaz_data[1].split('\n')[1]
        p_time = namaz_data[2].split('\n')[1]
        a_time = namaz_data[3].split('\n')[1]
        sh_time = namaz_data[4].split('\n')[1]
        kh_time = namaz_data[5].split('\n')[1]

        bomdod = f'🌅<i> Subuh</i>      :     <b>{b_time}</b>\n'
        peshin = f'☀<i> Duhur</i>       :     <b>{p_time}</b>\n'
        asr = f"⛅<i> Ashar</i>        :     <b>{a_time}</b>\n"
        shom = f'🏙<i> Maghrib</i>  :     <b> {sh_time}</b>\n'
        khuftan = f"🌃<i> Isya</i>           :      <b>{kh_time}</b>\n\n"
        sarchashma = f'<a href="{url}">Lihat sumber 👀</a>'
        self.message = f'Kotamu <b>{self.city}</b>\n\n' + bomdod + peshin + asr + shom + khuftan + sarchashma

    def parse_kz(self):
        from bs4 import BeautifulSoup
        import requests

        # Fetch the webpage HTML content
        url = self.kaz_cities[self.city]
        self.url = url
        response = requests.get(url)
        html_content = response.text

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all div tags with class "prayerTiles"
        prayer_tiles = soup.find_all('div', class_='prayerTiles')

        # Extract information from each prayer tile and store in separate arrays
        namaz_data = []

        for prayer_tile in prayer_tiles:
            # Extract the prayer name and time
            prayer_name = prayer_tile.find('p').text.strip()

            # Add to the prayer names and times arrays
            namaz_data.append(prayer_name)

        # Print the prayer names and times
        b_time = namaz_data[0].split('\n')[1] + ' - ' + namaz_data[1].split('\n')[1]
        p_time = namaz_data[2].split('\n')[1]
        a_time = namaz_data[3].split('\n')[1]
        sh_time = namaz_data[4].split('\n')[1]
        kh_time = namaz_data[5].split('\n')[1]

        bomdod = f'🌅<i> Фаджр</i>     :     <b>{b_time}</b>\n'
        peshin = f'☀<i> Зухр</i>          :     <b>{p_time}</b>\n'
        asr = f"⛅<i> Аср</i>            :     <b>{a_time}</b>\n"
        shom = f'🏙<i> Магриб</i>    :     <b> {sh_time}</b>\n'
        khuftan = f"🌃<i> Иша</i>          :      <b>{kh_time}</b>\n\n"
        sarchashma = f'<a href="{url}">Посмотреть источник 👀</a>'
        self.message = f'Ваш город <b>{self.city}</b>\n\n' + bomdod + peshin + asr + shom + khuftan + sarchashma

    def parse_uz(self):
        from bs4 import BeautifulSoup
        import requests

        # Fetch the webpage HTML content
        url = self.uzb_cities[self.city]
        self.url = url
        response = requests.get(url)
        html_content = response.text

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all div tags with class "prayerTiles"
        prayer_tiles = soup.find_all('div', class_='prayerTiles')

        # Extract information from each prayer tile and store in separate arrays
        namaz_data = []

        for prayer_tile in prayer_tiles:
            # Extract the prayer name and time
            prayer_name = prayer_tile.find('p').text.strip()

            # Add to the prayer names and times arrays
            namaz_data.append(prayer_name)

        # Print the prayer names and times
        b_time = namaz_data[0].split('\n')[1] + ' - ' + namaz_data[1].split('\n')[1]
        p_time = namaz_data[2].split('\n')[1]
        a_time = namaz_data[3].split('\n')[1]
        sh_time = namaz_data[4].split('\n')[1]
        kh_time = namaz_data[5].split('\n')[1]

        bomdod = f'🌅<i> Фаджр</i>     :     <b>{b_time}</b>\n'
        peshin = f'☀<i> Зухр</i>          :     <b>{p_time}</b>\n'
        asr = f"⛅<i> Аср</i>            :     <b>{a_time}</b>\n"
        shom = f'🏙<i> Магриб</i>    :     <b> {sh_time}</b>\n'
        khuftan = f"🌃<i> Иша</i>          :      <b>{kh_time}</b>\n\n"
        sarchashma = f'<a href="{url}">Посмотреть источник 👀</a>'
        self.message = f'Ваш город <b>{self.city}</b>\n\n' + bomdod + peshin + asr + shom + khuftan + sarchashma

    def send_to_all(self):
        import sqlite3
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM Users')
        users_data = cur.fetchall()
        this_func = {
            'tj': 'self.parse_tj()',
            'ru': 'self.parse_ru()',
            'ind': 'self.parse_ind()',
            'kz': 'self.parse_kz()',
            'uz': 'self.parse_uz()'
        }

        for user_data in users_data:
            self.user_id, self.name, self.username, self.country, self.city, self.url = user_data

            eval(this_func[self.country])
            function_str = f"bot.send_message({self.user_id},'''{self.message}''', parse_mode='html', disable_web_page_preview=True)"
            self.sending_list.append(function_str)


    def to_db(self):
        import sqlite3
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute("INSERT INTO Users(id, name, username, country, city, link) VALUES (?,?, ?,?,?,?)", (
            self.user_id, self.name, self.username, self.country, self.city, self.url))
        con.commit()
        cur.close()
        con.close()
