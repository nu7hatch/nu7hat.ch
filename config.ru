# -*- coding: undecided -*-
# -*- ruby -*-
require 'bundler/setup'
require 'sinatra'

BD = %q{
 _______________________________
< Czego szukasz ptysiu miętowy? >
 -------------------------------
    \
     \
    ^__^         /
    (oo)\_______/  _________
    (__)\       )=(  ____|_ \_____
        ||----w |  \ \     \_____ |
        ||     ||   ||           ||
}

set :public_folder, File.expand_path("../public", __FILE__)
set :views, File.expand_path("../views", __FILE__)

get "/" do
  File.read(File.join(settings.public_folder, "index.html"))
end

get "/bd" do
  @bd = BD
  erb :bd
end

get "/bd.txt" do
  content_type "text/plain"
  BD
end

not_found do
  File.read(File.join(settings.public_folder, "404.html"))
end

run Sinatra::Application
