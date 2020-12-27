# Rollin-Bot


> Về tác giả:

  Bạch Ngọc Minh Tâm và Nguyễn Minh Trí
  
  Một bot đơn giản để phục vụ trò chơi Truth or Dare cho nhóm bạn của tác giả.

> Cách sử dụng:

  Tạo một application mới trên https://discord.com/developers
  
  Sử dụng token từ bot vừa được tạo trên và chèn vào file bot.py
  
  Compile code và sử dụng thôi ^^
  
  Prefix mặc định của bot là ">", có thể edit ở file bt.py

Các chức năng chính:

> Lệnh roll

  Có 2 kiểu: " >roll " với mặc định là 5s và " >roll {số giây còn lại} "
  
  Thời gian roll tối thiểu là 5s và thời gian tối đa là 90s.

> Lệnh rollroom

  Có 2 kiểu: " >rollroom " với mặc định là 5s và " >rollroom {số giây còn lại} "
  
  Thời gian roll tối thiểu là 5s và thời gian tối đa là 90s.

> Lệnh listroom

  Trả về thông tin channel hiện tại mà người chơi đang tham gia.

> Lệnh remainTurn
  
  Có 2 kiểu: " >remainTurn " và " >remainTurn {số lượt ít nhất} {số lượt nhiều nhất} "
  
  Trả về số lượt chơi còn lại của trò chơi
  
  Giá trị trả về ít nhất 1 lượt chơi và tối đa 20 lượt chơi.
