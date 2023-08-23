export const convertDatetoUnixTimestamp = (date) => {
    return Math.floor(date.getTime()/1000);
};

export const convertUnixTimestamptoDate = (unixTimestamp) => {
    const milliseconds = unixTimestamp
    return new Date(milliseconds).toLocaleDateString("en-US");
};

export const createDate = (date, days, weeks, months, years) => {
    let newDate = new Date(date);
    newDate.setDate(newDate.getDate() + days + 7*weeks);
    newDate.setMonth(newDate.getDate() + months);
    newDate.setFullYear(newDate.getFullYear() + years);
    return newDate;
};