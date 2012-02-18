# -*- ruby -*- 
require 'bundler/setup'
require 'sinatra'

set :public_folder, File.expand_path("../public", __FILE__)

get "/" do
  File.read(File.join(settings.public_folder, "index.html"))
end

not_found do
  File.read(File.join(settings.public_folder, "404.html"))
end

run Sinatra::Application
