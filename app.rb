require 'rubygems'
require 'sinatra'

set :assets_path, File.expand_path('../assets', __FILE__)
set :public,      File.expand_path('../public', __FILE__)

get "/" do
  erb :'index.html'
end
