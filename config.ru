# -*- ruby -*- 
require 'bundler/setup'

use Rack::Static, {
  :root  => 'public',
  :index => 'index.html',
  :urls  => [""],
}

error_404 = 'public/404.html'

run lambda {
  [404, {
    "Content-Type"   => "text/html",
    "Content-Length" => File.size(error_404).to_s,
    "Last-Modified"  => File.mtime(error_404).httpdate,
    }, File.read(error_404)
  ]
}
