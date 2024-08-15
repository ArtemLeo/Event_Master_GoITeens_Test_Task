from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Зберігаємо події в списку
events = []


@app.route('/')
def home():
    return render_template('home.html', events=events)


@app.route('/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        description = request.form['description']
        events.append({'id': len(events) + 1, 'title': title, 'date': date, 'description': description})
        return redirect(url_for('home'))
    return render_template('create_event.html')


@app.route('/edit/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    event = next((event for event in events if event['id'] == event_id), None)
    if event is None:
        return redirect(url_for('home'))

    if request.method == 'POST':
        event['title'] = request.form['title']
        event['date'] = request.form['date']
        event['description'] = request.form['description']
        return redirect(url_for('home'))

    return render_template('edit_event.html', event=event)


@app.route('/delete/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    global events
    events = [event for event in events if event['id'] != event_id]
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
