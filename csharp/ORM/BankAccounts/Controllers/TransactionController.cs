using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using BankAccounts.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Identity;

namespace BankAccounts.Controllers
{
    [Route("transactions")]
    public class TransactionController : Controller
    {

        private int? UserSession
        {
            get { return HttpContext.Session.GetInt32("UserId"); }
            set { HttpContext.Session.SetInt32("UserId", (int)value); }
        }

        private List<Transaction> thisAccountTransactions
        {
            get{
                List<Transaction> currentUserAccount = dbContext.Transactions
                .Where(t => t.AccountHolderID == UserSession)
                .ToList();
                return currentUserAccount;
            }
        }

        private MyContext dbContext;
        public TransactionController(MyContext context)
        {
            dbContext = context;
        }

        [HttpGet("")]
        public IActionResult Index()
        {

            if(UserSession == null)
                return RedirectToAction("Index", "Home");

            if(HttpContext.Session.GetInt32("IsInvalidAmount") == 1)
            {
                ModelState.AddModelError("Transaction.Amount", "Please enter a valid dollar amount.");
                HttpContext.Session.SetInt32("IsInvalidAmount", 0);
            }

            if(HttpContext.Session.GetInt32("OverdrawAttempt") == 1)
            {
                ModelState.AddModelError("Transaction.Amount", "You cannot withdraw more than your available balance.");
                HttpContext.Session.SetInt32("OverdrawAttempt", 0);
            }

            

            AccountView currentUserAccountView = new AccountView()
            {
                Transactions = thisAccountTransactions
            };
            
            ViewBag.FirstName = HttpContext.Session.GetString("FirstName");
            ViewBag.Balance = thisAccountTransactions.Sum(t => t.Amount);
            ViewBag.AccountHolderID = UserSession;
            return View("Index", currentUserAccountView);
        }

        [HttpPost("transact")]
        public IActionResult Transact(AccountView thisTransaction)
        {
            if(ModelState.IsValid)
            {
                if((thisAccountTransactions.Sum(t => t.Amount) + thisTransaction.Transaction.Amount) >= 0)
                {
                    HttpContext.Session.SetInt32("IsInvalidAmount", 0);
                    thisTransaction.Transaction.AccountHolderID = (int)UserSession;
                    dbContext.Add(thisTransaction.Transaction);
                    dbContext.SaveChanges();
                }
                else
                {
                    HttpContext.Session.SetInt32("OverdrawAttempt", 1);
                    return RedirectToAction("Index");
                }
            }
            
            HttpContext.Session.SetInt32("IsInvalidAmount", 1);
            return RedirectToAction("Index");
        }
    }
}