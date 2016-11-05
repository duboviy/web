gem 'sinatra'
gem 'activerecord'
gem 'sqlite3'

require 'sinatra'
require 'active_record'
require 'sqlite3'
require 'json'


ActiveRecord::Base.establish_connection(
  :adapter => "sqlite3",
  :database => "hw.db"
)


class Blogpost < ActiveRecord::Base
end


# Get all the blogposts
get '/blogposts' do
  Blogpost.all.to_json
end

# Get one blogpost
get '/blogposts/:id' do
  Blogpost.find(params[:id]).to_json
end

# Create an blogpost
post '/blogposts' do
  @blogpost = Blogpost.new(params[:blogpost])
  @blogpost.save.to_json
end

# Update an blogpost
put '/blogposts/:id' do
  @blogpost = Blogpost.find(params[:id])
  @blogpost.update(params[:blogpost]).to_json
end

# Destroy the whole collection
delete '/blogposts' do
  Blogpost.all.map(&:destroy).to_json
end

# Destroy an blogpost
delete '/blogposts/:id' do
  Blogpost.find(params[:id]).destroy.to_json
end
