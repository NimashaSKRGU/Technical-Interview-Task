## API endpoints

- GET `/preload`: Load the GitHub data source and store it as a session variable (`item_list`). Preload function is called before any requests are served in order to load the data into `item_list` session variable.
- GET `/items` : return the session data from `item_list`
- POST `/items`: Add a new item to the `items_list` with the given form data. (With an incremental ID)
- DELETE `/items/{id}`: Remove the item with the given ID and update the session variable `item_list`

## Improvements

- Validate the form fields
- Use permanent storage instead of using session storage
