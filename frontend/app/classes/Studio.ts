class Studio {
    public readonly id: number;
    public readonly name: string;

    constructor(id: number, name: string) {
        this.id = id;
        this.name = name;
    }
}

class Branch {
    public readonly id: number;
    public readonly name: string;

    constructor(id: number, name: string) {
        this.id = id;
        this.name = name;
    }
}


// export default Studio;
export {Studio, Branch};