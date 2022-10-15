function slider() {
  let randomnumber = Math.floor(Math.random() * 3);
  let path = "Images\\SmartCurtainControl\\";
  let type = ".jpg";
  let images = [
    `${path}` + `smc1` + `${type}`,
    `${path}` + `smc2` + `${type}`,
    `${path}` + `smc3` + `${type}`,
  ];
  document.getElementById("slider1").src = images[randomnumber];
}
