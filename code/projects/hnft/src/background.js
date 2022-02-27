'use strict';

// With background scripts you can communicate with popup
// and contentScript files.
// For more information on background script,
// See https://developer.chrome.com/extensions/background_pages

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === 'GREETINGS') {
    const message = `Hi ${
      sender.tab ? 'Con' : 'Pop'
    }, my name is Bac. I am from Background. It's great to hear from you.`;

    // Log message coming from the `request` parameter
    console.log(request.payload.message);
    // Send a response message
    sendResponse({
      message,
    });
  }
});

const oneYearAgo = new Date() - 1000 * 60 * 60 * 24 * 365;
const historyConfig =
    { text: '', 'startTime': oneYearAgo, 'maxResults': 1000000 }

chrome.history.search(historyConfig,(data) => { historyProcesser(data)})


const historyProcesser = (data) => {    
    let domainMap = {}
    let historyList = []
    data.forEach((page) => { dataAdapters(page, domainMap, historyList) })
    
    console.log(JSON.stringify(domainMap))

    console.log(JSON.stringify(historyList))

    console.log("Generating nft ...")
    // generateNft(historyList)
    console.log("NFT generation complete!")
    
    return {domainMap,historyList}
}

const dataAdapters = (page, map, historyList) => {
    const { tilte, url, lastVisitTime, visitCount } = page;
    const domainName = extractRootDomain(url)
    historyList.push(domainName.replace(".","_"))
    if (domainName in map) {
        map[domainName] += visitCount;
    } else {
        map[domainName] = visitCount;
    }
}

const getFavIconUrlFromUrl = (url) => {
    return `https://t1.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=${url}&size=128`;
}

const extractHostname = (url) => {
    var hostname;
    //find & remove protocol (http, ftp, etc.) and get hostname
    if (url.indexOf("//") > -1) {
        hostname = url.split('/')[2];
    }
    else {
        hostname = url.split('/')[0];
    }
    //find & remove port number
    hostname = hostname.split(':')[0];
    //find & remove "?"
    hostname = hostname.split('?')[0];
    return hostname;
}

const extractRootDomain = (url) => {
    var domain = extractHostname(url),
        splitArr = domain.split('.'),
        arrLen = splitArr.length;

    //extracting the root domain here
    //if there is a subdomain 
    if (arrLen > 2) {
        domain = splitArr[arrLen - 2] + '.' + splitArr[arrLen - 1];
        //check to see if it's using a Country Code Top Level Domain (ccTLD) (i.e. ".me.uk")
        if (splitArr[arrLen - 2].length == 2 && splitArr[arrLen - 1].length == 2) {
            //this is using a ccTLD
            domain = splitArr[arrLen - 3] + '.' + domain;
        }
    }
    return domain;
}