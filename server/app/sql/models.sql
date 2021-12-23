-- model User
create table yogurt_users (
    user_id         serial primary key,
    user_name       varchar(50),
    password        varchar(50),
    email           varchar(50),
    avatar          varchar(100),
    yogurt_level    integer,
)