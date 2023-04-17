Array.prototype.last = function() {
    
    console.log(this);
    if(this.length > 0){
        
        for( var i =0; i<this.length; i++){
            if (i == this.length -1) return this[i]
        } 
    }
    
    return -1;
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */