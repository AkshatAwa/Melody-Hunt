import pywhatkit
from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config['MYSQL_PASSWORD'] = "1234567"
app.config['MYSQL_DB'] = "my_songs"
mysql = MySQL(app)


@app.route('/')
def login_page():
    while True:
        return render_template('login.html')


database = {"akshat": "2501", "sameer": "2502", "rushil": "2503"}


@app.route('/form_login', methods=['POST', 'GET'])
def login():
    while True:
        name1 = request.form['Username'].lower()
        pwd = request.form['Password']
        if name1 not in database:
            return render_template("login.html", info="Invalid UserName....Try Again")
        else:
            if database[name1] != pwd:
                return render_template("login.html", info="Invalid Password!...Try Again")
            else:
                return render_template('home.html', name=name1)


@app.route('/page2')
def page2():
    cursor = mysql.connection.cursor()
    cursor.execute("select Song_name from songs")
    data = cursor.fetchall()
    cursor.close()
    return render_template('page2.html', data=data)


@app.route('/page3')
def page3():
    return render_template("page3.html")


@app.route('/finding_lyrics', methods=['POST', 'GET'])
def finding_lyrics():
    while True:
        l1 = request.form["findlyrics"].lower()
        ac = mysql.connection.cursor()
        ab = mysql.connection.cursor()
        cursor = mysql.connection.cursor()
        ac.execute(f"select Song_name,Artist_name from songs where Lyrics='{l1}'")
        ab.execute(f"select Song_name from songs where Lyrics='{l1}'")
        cursor.execute("select Song_name from songs")
        data = cursor.fetchall()
        users = ac.fetchall()
        users2 = ab.fetchall()
        ac.close()
        ab.close()
        cursor.close()
        for a in users:
            pywhatkit.playonyt(users2)
            return render_template('page3.html', data=a)

        if l1 not in data:
            pywhatkit.playonyt(l1)
            return render_template('page3.html', data="We don't have this song in our database right now!! But we "
                                                      "will still guide you in finding the song;)")


@app.route('/page4')
def page4():
    return render_template("page4.html")


@app.route('/finding_song', methods=['POST', 'GET'])
def finding_songs():
    while True:
        l1 = request.form['findsong'].lower()
        ac = mysql.connection.cursor()
        ab = mysql.connection.cursor()
        cursor = mysql.connection.cursor()
        ac.execute(f"select Lyrics,Artist_name from songs where Song_name='{l1}'")
        ab.execute(f"select Song_name from songs where Song_name='{l1}'")
        cursor.execute("select Song_name from songs")
        data = cursor.fetchall()
        users = ac.fetchall()
        users2 = ab.fetchall()
        ac.close()
        ab.close()
        cursor.close()
        for a in users:
            pywhatkit.playonyt(users2)
            return render_template('page4.html', data=a)

        if l1 not in data:
            pywhatkit.playonyt(l1)
            return render_template('page4.html', data="We don't have this song's lyrics in our database right now!!")


@app.route('/page5')
def page5():
    return render_template("page5.html")


@app.route('/get_detail', methods=['POST', 'GET'])
def get_detail():
    a = request.form['Username'].lower()
    b = request.form['Hook-line'].lower()
    c = request.form['Artist name'].lower()
    ad = mysql.connection.cursor()
    ac = mysql.connection.cursor()
    ac.execute(f"select Song_name from songs where Song_name='{a}'")
    ad.execute(f"insert into songs value('{a}','{b}','{c}')")
    mysql.connection.commit()
    ae = ac.fetchall()
    ad.close()
    ac.close()
    if a==ae:
        return render_template("page5.html", info="This song is already in our playlist")
    else:
        return render_template("page5.html", info="Playlist has been Updated Successfully")


@app.route('/page6')
def page6():
    cursor = mysql.connection.cursor()
    cursor.execute("select Song_name from songs")
    data = cursor.fetchall()
    cursor.close()
    return render_template('page6.html', data=data)


@app.route('/remove_song', methods=['POST', 'GET'])
def remove_song():
    while True:
        a = request.form['remove-song'].lower()
        ad = mysql.connection.cursor()
        ad.execute(f"delete from songs where Song_name='{a}'")
        mysql.connection.commit()
        cursor = mysql.connection.cursor()
        cursor.execute("select Song_name from songs")
        data = cursor.fetchall()
        cursor.close()
        return render_template("page6.html", info="Playlist has been Updated Successfully", data=data)


@app.route('/page7')
def page7():
    a = login_page
    return a


if __name__ == '__main__':
    app.run(debug=True)
