const list = document.querySelector('.output ul');
list.innerHTML = '';
const stations = ['MAN675847583748sjt567654;Manchester Piccadilly',  //Desireed Output = MAN: Manchester Piccadilly
                  'GNF576746573fhdg4737dh4;Greenfield',
                  'LIV5hg65hd737456236dch46dg4;Liverpool Lime Street',
                  'SYB4f65hf75f736463;Stalybridge',
                  'HUD5767ghtyfyr4536dh45dg45dg3;Huddersfield'];

for (let station of stations) {
    
    const stationAbbr = station.slice(0,3); //MAN
    const stationCodeIndex = station.indexOf(';');  //# of char from ';'
    const stationCode = station.slice(0, stationCodeIndex-1); //576746573fhdg4737dh4
    const stationName = station.slice(stationCodeIndex+1); // Manchester Piccadilly
    const result = (`${stationAbbr} ${stationName}`)  // MAN Manchester Piccadilly
    
    const listItem = document.createElement('li');
    listItem.textContent = result;
    list.appendChild(listItem);
}
