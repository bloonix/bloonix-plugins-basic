#!/usr/bin/perl
use strict;
use warnings;
use Bloonix::IPC::Cmd;
use JSON;

my $options = {
    check_type => "multiple",
    command => {
        command => "check-http",
        timeout => 30,
        command_options => {
            url => "https://your-domain.test/",
            "user-agent" => "Bloonix Plugin Check-HTTP",
            critical => 10,
            warning => 5,
            timeout => 30
        }
    },
    service_id => 269,
    concurrency => 3,
    ssl_verify_mode => "none",
    ssl_ca_path => "/etc/ssl/certs",
    authkeys => {
        "localhost-1" => "secret",
        "localhost-2" => "secret",
        "localhost-3" => "secret"
    },
    locations => [
        {
            hostname => "localhost-1",
            ipaddr => "127.0.0.1"
        },
        {
            hostname => "localhost-2",
            ipaddr => "127.0.0.2"
        },
        {
            hostname => "localhost-3",
            ipaddr => "127.0.0.3"
        }
    ]
};

my $ipc = Bloonix::IPC::Cmd->run(
    command => "/usr/local/lib/bloonix/plugins/check-by-satellite --stdin --pretty",
    timeout => 150,
    kill_signal => 9,
    to_stdin => JSON->new->encode($options)
);

print join("\n", @{$ipc->stdout}), "\n";
print join("\n", @{$ipc->stderr}), "\n";
print "\n";
