console.log("The extension is up and running");

const oneYearAgo = new Date() - 1000 * 60 * 60 * 24 * 365;
const historyConfig =
    { text: '', 'startTime': oneYearAgo, 'maxResults': 1000000 };
chrome.history
    .search(historyConfig,
        (data) => {
            data.forEach((page) => {

            });
        });


const visitedPageProcesser = (data) => {
    
    data.forEach((page) => {

    })
}


