import axios from 'axios';
import Table from 'cli-table3';


const query = `
  query {
    characters {
      results {
        name
        status
        species
      }
    }
  }
`;


async function query_api() {
  try {
    const response = await axios.post('https://rickandmortyapi.com/graphql/', { query });
    return response.data.data.characters.results;
  } catch (error) {
    console.error(error);
  }
}


async function generate_csv_in_memory() {
  const data = await query_api()
  const table = new Table({
    head: ['Name', 'Status', 'Species'],
    colWidths: [20, 20, 20],
  });
  data.forEach(character => {
    table.push([character.name, character.status, character.species]);
  });
  return table
}


async function show_on_screen(){
    const table = await generate_csv_in_memory()
    console.log(table.toString());
}


show_on_screen()
