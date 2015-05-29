class MainController < ApplicationController
  def index
    render :index, layout: false
  end

  private

  def send_request
    a = HttpHandlerer.new
    post_result = a.send_setting(1, {a: 'stoil e gei', b: 'mavridis e gei'})
    result = a.get_with_id(1)
  end

  helper_method :send_request
end