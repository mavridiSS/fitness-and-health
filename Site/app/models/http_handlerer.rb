require 'net/http'
require 'uri'

class HttpHandlerer

  def get_program(id, data)
    send_setting(id, data)
    sleep(1)
    get_with_id(id)
  end

  def send_setting(id, data)
    data_array = {id: id, data: data}
    current_uri = uri_local(main_url + '/')
    https = Net::HTTP.new(current_uri.host, current_uri.port)
    req = Net::HTTP::Post.new(current_uri.path, {'Content-Type' =>'application/json'})
    req.body = data_array.to_json
    response = https.request(req)
  end

  def get_with_id(id)
    current_uri = uri_local(main_url + "/#{id}")
    response = Net::HTTP.get(current_uri)
  end

  private

  def main_url
    'http://localhost:8080'
  end

  def uri_local(route)
    URI.parse(route)
  end

  def header
    
  end
end