<h1>📚 StudyBud - Discussion Platform</h1>
<p><strong>StudyBud</strong> is a web application built with <strong>Django</strong> where users can join rooms, create discussions, and interact with other learners. It’s designed to make learning more collaborative, fun, and community-driven.</p>

<hr>

<h2>📌 Features</h2>
<ul>
  <li>✅ User authentication (Login, Register, Logout)</li>
  <li>✅ Create, update, and delete discussion rooms</li>
  <li>✅ Join rooms and participate in conversations</li>
  <li>✅ User profiles with activity feed</li>
  <li>✅ Search rooms by topic</li>
  <li>✅ Responsive and clean UI</li>
</ul>

<h2>🛠 Tech Stack</h2>
<ul>
  <li><strong>Backend:</strong> Python, Django</li>
  <li><strong>Frontend:</strong> HTML, CSS, Django Templates</li>
  <li><strong>Database:</strong> SQLite (can be upgraded to PostgreSQL/MySQL)</li>
  <li><strong>Tools:</strong> pip, venv</li>
</ul>

<h2>📁 Project Structure</h2>
<pre>
studybud/
├── base/                # Main Django app
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/       # HTML templates for base app
│       └── base/
│           ├── activity.html
│           ├── create_room.html
│           ├── delete_room.html
│           ├── feed_components.html
│           ├── home.html
│           ├── login_register.html
│           ├── profile.html
│           ├── topics.html
│           └── update-user.html
│
├── StudyBud/            # Project settings
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/              # CSS, JS, images
│
├── templates/           # Base templates
│   ├── main.html
│   └── navbar.html
│
├── manage.py
├── requirements.txt
└── README.md
</pre>

<h2>🚀 Installation</h2>
<p><strong>Prerequisites:</strong> Python 3.8+, pip</p>
<pre>
# Clone the repository
git clone https://github.com/your-username/studybud.git
cd studybud

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Start the server
python manage.py runserver
</pre>

<h2>🔗 Main Pages</h2>
<br>
<img width="1507" height="919" alt="Screenshot 2025-08-31 235116" src="https://github.com/user-attachments/assets/7a647a4a-bd23-4c46-82c1-9639642ef20e" />
 <br><br>

<h3>🏠 Home</h3>
<ul>
  <li>Displays available rooms</li>
  <li>Search by topic</li>
</ul>

<h3>💬 Room</h3>
<ul>
  <li>Join discussions in real-time</li>
  <li>Post and reply to messages</li>
</ul>

<h3>👤 Profile</h3>
<ul>
  <li>View user’s created rooms</li>
  <li>Activity feed of recent discussions</li>
</ul>

<h2>🧬 Models Overview</h2>

<h3>📝 Room</h3>
<ul>
  <li>host (User)</li>
  <li>topic (ForeignKey to Topic)</li>
  <li>name, description</li>
  <li>participants (Many-to-Many)</li>
  <li>updated, created (timestamps)</li>
</ul>

<h3>📌 Message</h3>
<ul>
  <li>user (ForeignKey to User)</li>
  <li>room (ForeignKey to Room)</li>
  <li>body</li>
  <li>updated, created (timestamps)</li>
</ul>

<h3>🏷 Topic</h3>
<ul>
  <li>name</li>
</ul>

<h2>🧪 Testing</h2>
<ul>
  <li>Run the server: http://127.0.0.1:8000/</li>
  <li>Admin Panel: http://127.0.0.1:8000/admin/</li>
  <li>Use the app’s UI to test discussions</li>
</ul>

<h2>🚧 Future Improvements</h2>
<ul>
  <li>[ ] Add real-time chat with WebSockets</li>
  <li>[ ] Add user avatars and profile customization</li>
  <li>[ ] Add notifications for replies</li>
  <li>[ ] Add pagination and filters</li>
  <li>[ ] Deploy to cloud (Heroku/AWS)</li>
</ul>



<h2>📜 License</h2>
<p>This project is licensed under the <a href="https://opensource.org/licenses/MIT">MIT License</a>.</p>
