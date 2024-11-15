
# /// script
# dependencies = ["nanodjango"]
# ///

from django.db import models
from nanodjango import Django


app = Django()

@app.admin
class CountLog(models.Model):
    # Standard Django model, registered with the admin site
    timestamp = models.DateTimeField(auto_now_add=True)

@app.route("/")
def count(request):
    # Standard Django function view
    CountLog.objects.create()
    return f"<p>Number of page loads: {CountLog.objects.count()}</p>"

@app.api.get("/add")
def add(request):
    # Django Ninja API support built in
    CountLog.objects.create()
    return {"count": CountLog.objects.count()}


if __name__ == "__main__":
    app.run(host="127.0.0.1")