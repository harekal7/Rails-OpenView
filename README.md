Rails OpenView
========

Open Associated View for methods in a controller in Rails.

### Installation for Sublime Text
#### Package Control (highly recommended)
Open command palette and type `Install Package` then type `Rails OpenView` and hit `Enter` or `Return`. Package Control will automatically download, install and update for you.

#### "git" command
Open your favourite Terminal application, browse to PACKAGES_PATH and run this command.

	git clone git://github.com/harekal7/Rails-OpenView.git

#### Manual Installation
Download .zip file from this repository and browse to PACKAGES_PATH, extract .zip file and rename folder to Rails-OpenView, restart Sublime Text if you are currently open.

** PACKAGES_PATH is referred to a folder which can be accessed via the `Preferences > Browse Packages...`

### Configuration
Open `Preferences > Key Bindings-User` and 
add `{ "keys": ["super+d"], "command": "rails_open_view" }`,

** You may use any other key bindings, whichever you will be comfortable with instead of `super+d`

### Usage

Whenever cursor is on a view name in controller, for example on `def index` or `redirect_to :action=>'index'` or `render :action => :new`, hit `super+d` to open `index.html.erb` ( that particular view )
