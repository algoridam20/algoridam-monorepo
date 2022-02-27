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
    console.log("NFT generation complete!")
    return {domainMap,historyList}
}

const dataAdapters = (page, map, historyList) => {
    const { tilte, url, lastVisitTime, visitCount } = page;
    const {hostname} = new URL(url)
    historyList.push(hostname.replace(".","_"))
    if (hostname in map) {
        map[hostname] += visitCount;
    } else {
        map[hostname] = visitCount;
    }
}

const getFavIconUrlFromUrl = (hostname) => {
    return `https://t2.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://https://${hostname}&size=128`;
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