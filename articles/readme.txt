Folder articles contain all articles (from 2021-01-01 to 2022-12-31) where company are mentioned in the text.
Each article is in 1 json file contain following fields:

{
  "_id": id of article
  "feed": // id of feed
  "title": // title
  "text": // text or article. contain some html tag for paragraph
  "published": published time in iso format,
  "tags": [ // company tag
    {
      "offsets": // positions in the text/title where company is mentioned,
      "name": // company name,
      "id": // isin code,
      "nexusId": // move digital id
    }
  ]
}
