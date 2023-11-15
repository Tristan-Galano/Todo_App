const { createApp } = Vue;

const Taskapp = {
  data() {
    return {
      task: {
        'name':''
      },
      tasks: [],
    };
  },
  async created() {
    await this.getTasks();
  },
  methods: {
    async getTasks() {
      const responce = await fetch(window.location, {
        method: "get",
        headers: {
          "X-Requsted-With": "XMLHttpRequest",
        },
      });

      this.tasks = await responce.json();
    },
    async createTask(){
        await this.getTasks()
        const responce = await fetch(window.location + 'create',{
            methods: 'post',
            headers:{
                'Content-Type': 'application/json',
                "X-Requsted-With": "XMLHttpRequest",
            },
            body: JSON.stringify(this.task)
        })

        await this.getTasks()
        
    }
  },
  delimiters: ["{", "}"],
};

createApp(Taskapp).mount("#app");
