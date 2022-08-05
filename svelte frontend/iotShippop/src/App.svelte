<script>
  // user client socket.io 
  import logo from './assets/sp-logo.svg'
  import { io } from "socket.io-client";
  let active = false;
  let imagePI = { imageSide1: {}, imageSide2: {} };

  //  connect to host server port:80
  const socket = io("http://20.205.123.195:80/");
  socket.on("connect", () => {
    console.log("connected!");
  });
  socket.on("sendstatus", (status) => {
    active = status;
    console.log(active);
  });
  socket.on("image", (imageFromPi) => {
    imagePI = imageFromPi;
    console.log(imagePI);
  });

  function clickButton() {
    active = !active;
    if (active == true) {
      imagePI = { imageSide1: {}, imageSide2: {} };
      socket.emit("image", imagePI);
    }
    socket.emit("sendstatus", active);
  }

  function toBase64(arrayBuffer) {
    var base64 = btoa(
      new Uint8Array(arrayBuffer).reduce(
        (data, byte) => data + String.fromCharCode(byte),
        ""
      )
    );
    return base64;
  }
</script>

<main>
  <img style="width: 30%;" src={logo} alt="Shippop Logo" >
  <div class="container">
    <div class="imageCard">
      <img src="data:image/png;base64,{toBase64(imagePI.imageSide1.image0)}" alt=""/>
      <img src="data:image/png;base64,{toBase64(imagePI.imageSide1.image1)}" alt=""/>
      <img src="data:image/png;base64,{toBase64(imagePI.imageSide1.image2)}" alt=""/>
      <p>Side1</p>
    </div>
    <div class="imageCard">
      <img src="data:image/png;base64,{toBase64(imagePI.imageSide2.image0)}" alt=""/>
      <img src="data:image/png;base64,{toBase64(imagePI.imageSide2.image1)}" alt=""/>
      <img src="data:image/png;base64,{toBase64(imagePI.imageSide2.image2)}" alt=""/>
      <p>Side2</p>
    </div>
  </div>

  <div>
    <button class:active on:click={clickButton}> START</button>
    <p>
      raspi start record = {active}
    </p>
  </div>
</main>


<style>
  .active {
    background-color: rgb(79, 221, 79);
  }
  .container{
    width: 540px;
    height: auto;
    border: 20px solid rgb(4,156,252,0.5);
    background-color: rgb(4,156,252,0.5);
    display: grid;
    grid-template-columns: 220px 220px;
    grid-gap: 100px;
    
  }
  .container > .imageCard img{
    max-width: 100%;
    background: fixed;
  }

</style>
