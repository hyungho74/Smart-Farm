const express = require('express');
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const path = require('path');

// 정적 파일 디렉토리 설정
app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname + '/../../sockets/web/index.html'));
});

// 클라이언트 연결 이벤트 처리
io.on('connection', (socket) => {
  console.log('new client connected.');

  // 센서 데이터 수신 이벤트 처리
  socket.on('sensor_data', (data) => {
    console.log('새로운 센서 데이터:', data);
    // 클라이언트에게 센서 데이터 전송
    io.emit('update_sensor_data', data);
  });

  // 클라이언트 연결 해제 이벤트 처리
  socket.on('disconnect', () => {
    console.log('disconnect');
  });
});

// 서버 시작
const port = 3000;
http.listen(port, () => {
  console.log(`서버가 포트 ${port}에서 실행 중입니다.`);
});
