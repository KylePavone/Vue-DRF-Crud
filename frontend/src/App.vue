<template>
  <div id="app">

  <form @submit.prevent="submitForm">
    <div class="form-group row">
        <input type="text" class="form-control  mx-2" placeholder="Name" v-model="player.name">
        <input type="text" class="form-control  mx-2" placeholder="Game" v-model="player.game">
        <input type="text" class="form-control  mx-2" placeholder="Rating" v-model="player.rating">
        <button type="submit" class="btn btn-success">Submit</button>
    </div>
  </form>



    <table class="table">
        <thead>
            <th>Name</th>
            <th>Game</th>
            <th>Rating</th>
        </thead>
        <tbody>
            <tr v-for="player in players" :key="player.id" @dblclick="$data.player=player">
                <td>{{ player.name }}</td>
                <td>{{ player.game }}</td>
                <td>{{ player.rating }}</td>
                <button class="btn btn-outline-danger" @click="deletePlayer(player)">x</button>
            </tr>
        </tbody>
    </table>
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return {
        player: {},
        players: []
    }
  }, async created(){
        await this.getPlayers();
  },

  methods: {
    submitForm(){
        if(this.player.id === undefined){
            this.createPlayer();
        } else{
            this.editPlayer();
        }
    },
    async getPlayers(){
        var response = await fetch('http://127.0.0.1:8000/api/players/');
        this.players = await response.json();
    },
    async createPlayer(){
            await this.getPlayers();
                                        
            await fetch('http://127.0.0.1:8000/api/players/', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.player)
        });
            await this.get.Players();
    },
    async editPlayer(){
            await this.getPlayers();

            await fetch(`http://127.0.0.1:8000/api/players/${this.player.id}`, {
            method: 'put',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.player)
        });
        await this.getPlayers();
        this.players = {};
    },
    async deletePlayer(player){
            await this.getPlayers();

            await fetch(`http://127.0.0.1:8000/api/players/${player.id}`, {
            method: 'delete',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.player)
        });
        await this.getPlayer();
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
